# LLM-IN-LANGCHAIN

A simple LangChain project demonstrating integration with Google Gemini.

## Prerequisites

Make sure you have the following installed:

* Python 3.10+
* Git
* Google Gemini API Key

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/utkarshyashraj/LLM-IN-LANGCHAIN.git
cd LLM-IN-LANGCHAIN
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv myenv
```

### 3. Activate the virtual environment

Windows:

```bash
myenv\Scripts\activate
```

After activation, you should see `(myenv)` in your terminal.

### 4. Install dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

### 5. Create the `.env` file

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace `your_gemini_api_key_here` with your actual Gemini API key.

**Do not commit your `.env` file to GitHub.**

### 6. Configure the model

The Gemini model configuration is available in `config.json`:

```json
{
    "provider": "gemini",
    "gemini": {
        "model": "gemini-3.5-flash",
        "temperature": 0.7,
        "max_output_tokens": 200
    }
}
```

### 7. Run the application

```bash
python app.py
```

The application will initialize the LangChain Gemini model and send a sample prompt.

## Project Structure

```text
LLM-IN-LANGCHAIN/
│
├── app.py              # Main application
├── llm_factory.py      # Creates and configures the LLM
├── config.json         # Model configuration
├── requirements.txt    # Python dependencies
├── rough.py            # Experimental/testing code
├── README.md           # Project documentation
├── .gitignore          # Git ignore rules
└── .env                # API key (not committed)
```

## How It Works

The application follows this flow:

```text
app.py
   ↓
llm_factory.py
   ↓
config.json
   ↓
ChatGoogleGenerativeAI
   ↓
Google Gemini
   ↓
AI Response
```

## Environment Variables

| Variable         | Description           |
| ---------------- | --------------------- |
| `GEMINI_API_KEY` | Google Gemini API key |

## Dependencies

Dependencies are maintained in `requirements.txt`.

Install them using:

```bash
pip install -r requirements.txt
```

## Git Ignore

Make sure `.env` is included in `.gitignore`:

```text
.env
myenv/
__pycache__/
```

## License

MIT License
