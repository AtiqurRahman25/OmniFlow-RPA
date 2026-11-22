
# DHL Invoice Information Extraction

## 1. Email Trigger Configuration

The workflow uses a **Gmail Trigger** to monitor incoming emails.

The trigger will only process emails that match the predefined conditions based on the email subject and body.

### Email Filtering Conditions
- The email subject and body must match the defined conditions.
- For example, emails containing **"DHL Invoice Information"** in the subject will be considered for processing.
- Emails that do not meet the predefined conditions will be ignored.

## 2. PDF Attachment Processing

Once an email meets the filtering conditions:

1. The workflow will identify the PDF attachment.
2. The PDF file will be downloaded and stored in the designated local folder.
3. The stored PDF will be passed to the LLM for information extraction.

## 3. Information Extraction

The LLM will analyze the PDF document and extract the following four key information fields:

| # | Field Name | Description |
|---|---|---|
| 1 | Challan No | Unique challan/reference number |
| 2 | Date | Challan or invoice date |
| 3 | Total Challan Amount | Total amount mentioned in the challan |
| 4 | DHL TDS Amount | Total TDS amount applicable to DHL |

## 4. Document Quality & Confidence Scoring

The PDF document may contain scanned images that are fuzzy, blurry, or unclear. This may affect the accuracy of information extraction.

To address this issue, the workflow will include an **LLM Confidence Score** for the extracted information.

### Confidence Score
- The LLM will evaluate how confident it is about the extracted information.
- A confidence score will indicate the reliability of the extracted data.
- Low-confidence results may indicate unclear images, poor document quality, or ambiguous information.
- Results with low confidence should be flagged for manual verification.

### Expected Output

The extraction process will produce the following information:

| Field | Extracted Value |
|---|---|
| Challan No | Extracted Challan Number |
| Date | Extracted Date |
| Total Challan Amount | Extracted Amount |
| DHL TDS Amount | Extracted TDS Amount |
| LLM Confidence Score | Confidence Score |

**Note:** Confidence scores represent the LLM's estimated certainty, not a guarantee of extraction accuracy.

## 5. Process Flow

1. Gmail Trigger monitors incoming emails.
2. Email subject and body are checked against predefined conditions.
3. Non-matching emails are ignored.
4. Matching emails are checked for PDF attachments.
5. PDF attachments are downloaded and stored in the local folder.
6. The LLM analyzes the PDF document.
7. Four required information fields are extracted.
8. An LLM confidence score is generated.
9. Low-confidence results are flagged for manual verification.
