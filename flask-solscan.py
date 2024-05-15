import requests
import json
import pandas as pd
from datetime import datetime
from flask import Flask, request, render_template_string, send_file
import io

app = Flask(__name__)

@app.route('/<address>', methods=['GET'])
def get_transactions(address):
    if not address:
        return "Error: No address provided. Please specify an address parameter."

    url = f"https://api.solscan.io/v2/account/transaction?address={address}&limit=99999999"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://solscan.io/",
        "sol-aut": "CgbRB9dls0fKMv0unROae4qWGpfgG0wj-ZYZYCLT",
        "Priority": "u=4",
        "Origin": "https://solscan.io",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        transactions = data["data"]["transactions"]
        extracted_data = []
        for tx in transactions:
            signature = tx.get("txHash", "")
            block = tx.get("slot", "")
            timestamp = tx.get("blockTime", "")
            time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') if timestamp else ""
            instructions_set = sorted(set(instr.get("type", "") for instr in tx.get("parsedInstruction", [])))
            instructions = ", ".join(instructions_set)
            by = ", ".join(tx.get("signer", []))
            fee_sol = tx.get("fee", 0) / 1e9  # Convert from lamports to SOL

            extracted_data.append({
                "Signature": signature,
                "Block": block,
                "Time": time,
                "Instructions": instructions,
                "By": by,
                "Fee (SOL)": format(fee_sol, '.9f')  # Format to 9 decimal places
            })

        # Convert to DataFrame
        df = pd.DataFrame(extracted_data)

        # Convert DataFrame to CSV with tab delimiter
        csv_data = df.to_csv(index=False, sep='\t', float_format='%.9f')

        return render_template_string(TEMPLATE, csv_data=csv_data, address=address)
    else:
        return f"Failed to retrieve data. Status code: {response.status_code}"

@app.route('/download/<address>', methods=['GET'])
def download_csv(address):
    if not address:
        return "Error: No address provided. Please specify an address parameter."

    url = f"https://api.solscan.io/v2/account/transaction?address={address}&limit=99999999"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://solscan.io/",
        "sol-aut": "CgbRB9dls0fKMv0unROae4qWGpfgG0wj-ZYZYCLT",
        "Priority": "u=4",
        "Origin": "https://solscan.io",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        transactions = data["data"]["transactions"]
        extracted_data = []
        for tx in transactions:
            signature = tx.get("txHash", "")
            block = tx.get("slot", "")
            timestamp = tx.get("blockTime", "")
            time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') if timestamp else ""
            instructions_set = sorted(set(instr.get("type", "") for instr in tx.get("parsedInstruction", [])))
            instructions = ", ".join(instructions_set)
            by = ", ".join(tx.get("signer", []))
            fee_sol = tx.get("fee", 0) / 1e9  # Convert from lamports to SOL

            extracted_data.append({
                "Signature": signature,
                "Block": block,
                "Time": time,
                "Instructions": instructions,
                "By": by,
                "Fee (SOL)": format(fee_sol, '.9f')  # Format to 9 decimal places
            })

        # Convert to DataFrame
        df = pd.DataFrame(extracted_data)

        # Save to a CSV in memory with tab delimiter
        output = io.BytesIO()
        df.to_csv(output, index=False, sep='\t', float_format='%.9f')
        output.seek(0)

        return send_file(output, mimetype='text/csv', download_name='transactions.csv', as_attachment=True)
    else:
        return f"Failed to retrieve data. Status code: {response.status_code}"

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Transactions Table</title>
    <!-- DataTables CSS -->
    <link rel="stylesheet" href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css">
    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <!-- DataTables JS -->
    <script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
</head>
<body>
    <h1>Transactions Table</h1>
    <table id="transactions" class="display" style="width:100%">
        <thead>
            <tr>
                <th>Signature</th>
                <th>Block</th>
                <th>Time</th>
                <th>Instructions</th>
                <th>By</th>
                <th>Fee (SOL)</th>
            </tr>
        </thead>
        <tbody>
            {% for row in csv_data.splitlines()[1:] %}
                <tr>
                    {% for cell in row.split('\t') %}
                        <td>{{ cell }}</td>
                    {% endfor %}
                </tr>
            {% endfor %}
        </tbody>
    </table>
    <button onclick="window.location.href='/download/{{ address }}'">Download CSV</button>
    <script>
        $(document).ready(function() {
            $('#transactions').DataTable();
        });
    </script>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
