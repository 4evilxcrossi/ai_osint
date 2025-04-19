import openai

# Optional: Store your key securely in .env
openai.api_key = "sk-"  # Replace with your key or load from env

def analyze_recon(target_type, target, recon_results):
    """
    target_type: 'username' or 'email'
    target: the actual username/email
    recon_results: list of findings (each string is a recon output line)
    """

    prompt = f"""
You are an OSINT analysis AI. Your task is to analyze reconnaissance results for a given {target_type} and produce:
- A summarized profile
- Noteworthy findings
- Threat level (Low / Medium / High)

Target: {target}
Findings:
{chr(10).join(recon_results)}

Return the summary in Markdown format with sections: **Profile**, **Findings**, **Threat Level**, **Advice**
"""

    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            temperature=0.2,
            max_tokens=2000  # You can adjust the token limit as needed
        )

        summary = response.choices[0].text.strip()
        return summary

    except Exception as e:
        return f"[!] AI analysis failed: {e}"
