# Etherscan Contract Verification Script

This script automates the process of verifying a Solidity smart contract on Etherscan. It combines submitting the verification request and checking the verification status, making it more convenient to verify contracts programmatically without needing to manually copy GUIDs between steps.

## Requirements

- Python 3.x
- `requests` library

To install the `requests` library, run:
```sh
pip install requests
```

## Usage

### 1. Update the Script with Your Contract Details

Modify the `etherscan_verify.py` script to include your contract details:

- **API Key**: Replace `YourApiKeyToken` with your actual Etherscan API key.
- **Contract Source Code File**: Specify the path to your flattened Solidity file, such as `contracts/mtb_flattened.sol`.
- **Contract Address**: Replace `0xYourContractAddress` with the address where your contract is deployed.
- **Contract Name**: Replace `MTB` with the name of your contract.
- **Compiler Version**: Use the exact version of the Solidity compiler that was used during deployment, e.g., `v0.6.12+commit.27d51765`.
- **Optimization Settings**: Set `optimization_used` to `'1'` if you used optimization during compilation, or `'0'` if not. Also, provide the number of optimization runs.

### 2. Run the Script

To run the script, use:
```sh
python3 etherscan_verify.py
```

The script will:
1. Submit a verification request to Etherscan.
2. Periodically check the verification status until it's either successful or fails.

### Example Configuration

```python
# Main script
if __name__ == "__main__":
    api_key = "YourApiKeyToken"
    source_code_file = "contracts/mtb_flattened.sol"
    contract_address = "0xYourContractAddress"
    contract_name = "MTB"
    compiler_version = "v0.6.12+commit.27d51765"
    optimization_used = "1"
    runs = "200"
```

## Notes

- **Flattened Contract**: Make sure your contract file is flattened, meaning it should contain only one contract definition without external imports.
- **Contract Name**: The `contract_name` must exactly match the name defined in your Solidity file.
- **Path Formatting**: Only specify the contract name without the file path (e.g., `MTB`).
- **Compiler Version**: Ensure the compiler version is an exact match with what was used for deployment.

## Troubleshooting

- If the script returns an error such as "Unable to locate ContractName," ensure the contract name matches exactly as defined in the Solidity file.
- You can also try manually verifying the contract through the Etherscan website to gain more insight into any potential issues.

## License

This script is open-source and available for personal or commercial use under the MIT License.


