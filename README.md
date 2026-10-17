# LangGraph_Codes

A LangChain workflow that generates a job description from a hiring request using OpenAI, then loops through an approval step before posting it.

## Run

```bash
pip install langchain-core langchain-openai python-dotenv
echo "OPENAI_API_KEY=your_key" > .env
python jdbyLangchain.py
```
