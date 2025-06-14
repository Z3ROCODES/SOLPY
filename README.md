
# Solana Token Manager CLI

A Python command-line tool to help you manage Solana wallets, tokens, minting, metadata, and transfers using the Solana CLI and SPL Token commands inside a Docker container.

## Features

- View your Solana address and balance
- Create and save mint addresses
- Manage token metadata (profile images, descriptions)
- Mint tokens on DevNet
- Transfer tokens between accounts
- Disable minting (for marketplace use)
- Helpful links for Solana tools and resources
- Automated Docker setup for environment consistency

## Prerequisites

- Docker installed (the script can help you install it on Ubuntu)
- Basic knowledge of Solana CLI and SPL Token commands

## Usage

1. Run the script:  
   ```bash
   python3 main.py
   ```

2. Follow the interactive menu to perform tasks like creating mint addresses, minting tokens, changing metadata, etc.

3. The script manages a Docker container running the Solana environment, so you don't need to manually configure dependencies.

## Notes

- Make sure to use square profile images (512x512 or 1024x1024) under 100KB for metadata.
- The script supports both DevNet and MainNet connections.
- Mint disabling is only available on MainNet.

## Author

Created by [By Z3ROCODES]
Credits For NetworkChuck For telling me all about this info
his video: https://www.youtube.com/watch?v=L4ASwqLZVV0