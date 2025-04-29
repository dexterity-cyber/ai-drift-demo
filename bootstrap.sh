#!/bin/bash

echo "🚀 Starting full bootstrap..."

# Check if requirements.txt exists
if [ ! -f requirements.txt ]; then
  echo "❌ Missing requirements.txt — aborting."
  exit 1
fi

# Step 1: Create virtual environment
echo "🔧 Creating virtualenv..."
python3 -m venv .venv

# Step 2: Activate it (inline for bash users)
source .venv/bin/activate

# Step 3: Install dependencies
echo "📦 Installing dependencies from requirements.txt..."
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt

# Step 4: Check for model
echo "📁 Checking model path..."
if ls models/*.gguf 1> /dev/null 2>&1; then
  echo "✅ Found GGUF model file in models/."
else
  echo "⚠️  No GGUF model found in models/. Place your .gguf Llama model there before running 'make baseline'."
fi

# Step 5: Summary
echo "✅ Bootstrap complete. Run 'make baseline' or 'make demo' next!"