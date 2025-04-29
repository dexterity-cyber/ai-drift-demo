#!/bin/bash

echo "🧹 Cleaning old environment and outputs..."

# Remove old virtualenv and JSON outputs
rm -rf .venv baseline.json drift.json

echo "✅ Removed .venv and JSON files."

# Create new virtualenv
python3 -m venv .venv
source .venv/bin/activate

echo "✅ New virtualenv created and activated."

# Install dependencies
echo "📦 Installing packages..."
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt

echo "✅ Setup complete. Ready to run 'make baseline' or 'make demo'."