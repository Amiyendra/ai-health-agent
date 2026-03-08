# 🩺 MediGraph: Multi-Agent Clinical Safety System

**Built for AI for Bharat Prototype Development Phase** *Preventing Adverse Drug Events with Autonomous AI Orchestration*

---

## 💡 The Problem
Every year, millions of preventable adverse drug events occur because patient medical histories (EHR) and complex pharmacological guidelines exist in isolated silos. Doctors have mere minutes to cross-reference fragmented data, leading to fatal prescription errors.

## 🚀 The Solution
**MediGraph** is a serverless, multi-agent clinical decision support system. It acts as an AI Copilot that evaluates proposed treatments by synthesizing deterministic patient data with unstructured medical literature in real-time.

### 🧠 Key Features
- **Zero-Hallucination Verdicts:** Uses RAG (Retrieval-Augmented Generation) and direct database queries to ensure accuracy.
- **Multi-Agent Orchestration:** Powered by **Amazon Bedrock (Nova Pro)** to coordinate specialized sub-agents.
- **Real-Time Traceability:** Doctors can see the live "thinking process" of the agents.
- **Fully Serverless:** Highly scalable architecture using AWS Lambda, DynamoDB, and OpenSearch.

---

## 🛠️ Technical Architecture

[Image of AWS Serverless Multi-Agent Architecture for Healthcare]

1. **Supervisor Agent (Amazon Bedrock):** The brain of the system that analyzes the doctor's intent.
2. **EHR Specialist Agent:** Triggers **AWS Lambda** to securely fetch patient records from **Amazon DynamoDB**.
3. **Medical Researcher Agent:** Uses **RAG** via **Amazon OpenSearch Serverless** to extract guidelines from medical PDFs stored in **Amazon S3**.
4. **Synthesis Engine:** Consolidates findings to issue a "SAFE" or "CRITICAL WARNING" verdict.

---

## 💻 Tech Stack
- **Frontend:** Next.js (React), Tailwind CSS, Framer Motion (Deployed on Vercel)
- **Backend:** FastAPI (Python), Boto3 (Deployed on Render)
- **AI/ML:** Amazon Bedrock (Nova Pro), Amazon OpenSearch (Vector DB)
- **Infrastructure:** AWS Lambda, Amazon DynamoDB, Amazon S3

---

## 🏃‍♂️ Getting Started
### Prerequisites
- Python 3.9+
- Node.js 18+
- AWS Credentials with Bedrock Access
https://github.com/Amiyendra/ai-health-agent.git
Setup Backend:

Bash
cd backend && pip install -r requirements.txt
uvicorn server:app --reload
Setup Frontend:

Bash
cd frontend && npm install
npm run dev


