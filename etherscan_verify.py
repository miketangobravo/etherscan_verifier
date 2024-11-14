import requests
import time

# Function to submit the contract verification request
def submit_verification(api_key, source_code_file, contract_address, contract_name, compiler_version, optimization_used, runs):
    url = "https://api.basescan.org/api"

    # Read the contract source code from file
    with open(source_code_file, 'r') as file:
        source_code = file.read()


    params = {
        'module': 'contract',
        'action': 'verifysourcecode',
        'apikey': api_key,
        'codeformat': 'solidity-single-file',  # Use 'solidity-standard-json-input' for JSON format
        'sourceCode': source_code,
        'contractname': contract_name,
        'compilerversion': compiler_version,
        'optimizationUsed': optimization_used,  # 0 for no optimization, 1 for optimization used
        'runs': runs,  # Number of optimization runs
        'evmversion': '',  # Leave empty for default EVM version or specify one of the available options
        'contractaddress': contract_address,  # Address where the contract is deployed
    }
    # Submit verification request
    response = requests.post(url, data=params)

    if response.status_code == 200:
        response_json = response.json()
        if response_json.get('status') == '1':
            guid = response_json.get('result')
            print("Verification request submitted successfully.")
            return guid
        else:
            print("Verification submission failed:", response_json.get('result'))
            return None
    else:
        print("Error:", response.status_code, response.text)
        return None

# Function to check the verification status
def check_verification_status(api_key, guid):
    url = "https://api.basescan.org/api"
    params = {
        'module': 'contract',
        'action': 'checkverifystatus',
        'guid': guid,
        'apikey': api_key,
    }

    while True:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            response_json = response.json()
            status = response_json.get('status')
            if status == '1':
                print("Verification successful:", response_json.get('result'))
                break
            elif status == '0':
                print("Verification in progress:", response_json.get('result'))
                time.sleep(10)  # Wait for 10 seconds before checking again
            else:
                print("Verification failed:", response_json.get('result'))
                break
        else:
            print("Error:", response.status_code, response.text)
            break

# Main script
if __name__ == "__main__":
    # Replace with your actual details
    api_key = "INSERTAR API KEY"
    source_code_file = "contracts/mtb_flattened.sol"
    contract_address = "0x2b1A955b2C8B49579d197eAaa7DcE7DBC7b4dA23"
    contract_name = "contracts/mtb_flattened.sol:MTB"  # Replace with the correct contract name
    compiler_version = "v0.6.12+commit.27d51765"
    optimization_used = "1"
    runs = "200"

    # Submit the verification request
    guid = submit_verification(api_key, source_code_file, contract_address, contract_name, compiler_version, optimization_used, runs)

    # If the request was submitted successfully, check the verification status
    if guid:
        check_verification_status(api_key, guid)

