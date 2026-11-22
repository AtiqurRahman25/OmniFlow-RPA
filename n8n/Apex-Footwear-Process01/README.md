# Email Trigger Configuration

## Process 1: Responsible Person
**Responsible Person:** Mr. Nafiz Imtiaz

**LinkedIn:** [Mr. Nafiz Imtiaz](https://www.linkedin.com/in/nafiz-imtiaz-mba-aust/)

## Current Status
Currently, the workflow uses a **Gmail Trigger** to monitor incoming emails.

## Planned Configuration
The Gmail Trigger will be replaced with an **Outlook Trigger** because Apex requires Outlook integration instead of Gmail.

The Outlook integration is currently pending the required credentials. Once the credentials are received, the Outlook Trigger will be configured accordingly.

## Email Filtering Logic
Incoming emails will be filtered based on the sender's email domain. Only emails originating from the following four bank domains will be processed:

- `@citybankplc.com`
- `@ebl-bd.com`
- `@bankasia-bd.com`
- `@uttarabank-bd.com`

### Filtering Rules
- Emails from the four specified bank domains will be accepted and processed.
- Emails from all other domains will be ignored.

## N8N Workflow 
<img width="618" height="305" alt="Gmail-Attachment" src="https://github.com/user-attachments/assets/3c5d4d9d-087d-4090-9c48-8739cece1819" />

## Excel Population info Extracted from Attachments

<img width="667" height="69" alt="Excel-Update" src="https://github.com/user-attachments/assets/c1144da9-979b-4272-afb4-4c2d3b5acdd7" />
