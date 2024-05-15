import requests
import json
import pandas as pd
from datetime import datetime
from flask import Flask, request, send_file
import io

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_transactions():
    # Get the SOL contract address from the URL parameter
    address = request.args.get('address')
    if not address:
        return "Error: No address provided. Please specify an address parameter."

    url = f"https://api.solscan.io/v2/account/transaction?address={address}&limit=10"
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

    # Check the status code
    if response.status_code == 200:
        data = response.json()

        # Extract the relevant information
        transactions = data["data"]["transactions"]
        extracted_data = []
        for tx in transactions:
            signature = tx.get("txHash", "")
            block = tx.get("slot", "")
            timestamp = tx.get("blockTime", "")
            time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') if timestamp else ""
            instructions_set = {instr.get("type", "") for instr in tx.get("parsedInstruction", [])}
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

        # Save to a CSV in memory
        output = io.StringIO()
        df.to_csv(output, index=False, float_format='%.9f')
        output.seek(0)

        return send_file(output, mimetype='text/csv', attachment_filename='transactions.csv', as_attachment=True)
    else:
        return f"Failed to retrieve data. Status code: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)
