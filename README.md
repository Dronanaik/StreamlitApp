# Streamlit Apps Collection

This repository contains a collection of interactive Streamlit applications demonstrating various algorithms and concepts.

## 📱 Applications

### 1. Byte Pair Encoding (BPE) Demo
**File:** `Byte-Pair-Encoding-Algo.py`

An interactive demonstration of the Byte Pair Encoding algorithm used in natural language processing and tokenization. This app shows step-by-step how BPE works by merging the most frequent character pairs in text.

**Features:**
- Interactive text input
- Configurable number of merge operations
- Step-by-step visualization of the BPE process
- Real-time vocabulary updates

### 2. Minimum Edit Distance Calculator
**File:** `minimueditdistance.py`

A calculator that computes the minimum edit distance between two strings using dynamic programming. Shows the exact operations (insert, delete, replace) needed to transform one string into another.

**Features:**
- Interactive string input
- Detailed edit operations breakdown
- Dynamic programming visualization
- Algorithm explanation

### 3. OpenRouter Chatbot
**File:** `openrouter-api-use.py`

A conversational AI chatbot powered by OpenRouter API. Designed as a Python coding assistant that provides structured code examples and explanations.

**Features:**
- Chat-based interface
- Python code generation and explanation
- Structured tutorial format
- OpenRouter API integration

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Streamlit
- Required dependencies (see individual files for specific imports)

### Installation
1. Clone this repository
2. Install dependencies:
   ```bash
   pip install streamlit pandas numpy openai
   ```

### Running the Apps
Each app can be run independently using Streamlit:

```bash
# Run BPE Demo
streamlit run Byte-Pair-Encoding-Algo.py

# Run Edit Distance Calculator
streamlit run minimueditdistance.py

# Run OpenRouter Chatbot (requires API key setup)
streamlit run openrouter-api-use.py
```

## 📋 Requirements

- `streamlit` - Web app framework
- `pandas` - Data manipulation
- `numpy` - Numerical computing
- `openai` - OpenAI API client (for OpenRouter chatbot)

## 🔧 Configuration

For the OpenRouter chatbot, you'll need to:
1. Get an API key from [OpenRouter](https://openrouter.ai/)
2. Replace `YOUR_API_KEY` in the code with your actual API key
3. Optionally use Streamlit secrets for secure key management

## 📚 Educational Value

These applications are designed for educational purposes and demonstrate:
- Algorithm visualization
- Interactive web app development with Streamlit
- API integration
- Dynamic programming concepts
- Natural language processing techniques

## 🤝 Contributing

Feel free to contribute by:
- Adding new streamlit applications
- Improving existing algorithms
- Enhancing the user interface
- Adding documentation

## 📄 License

This project is open source and available under the MIT License.
