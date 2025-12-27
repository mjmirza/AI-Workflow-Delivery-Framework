# Templates Index
## Ready-to-Use Business Documents

---

## Available Templates

| # | Template | Purpose | Formats |
|---|----------|---------|---------|
| 1 | Scope of Work | Project definition & deliverables | MD, HTML |
| 2 | Service Agreement | Legal contract | MD, HTML |
| 3 | Retainer Agreement | Ongoing maintenance | MD, HTML |
| 4 | Invoice Templates | Billing documents | MD, HTML |
| 5 | Email Templates | Communication scripts | MD |
| 6 | Proposal Template | Sales proposals | MD, HTML |
| 7 | Project Brief | Quick project summary | MD, HTML |
| 8 | Handover Checklist | Delivery document | MD |
| 9 | Change Order | Project scope modifications | MD |

---

## Converting to Word & PDF

### Method 1: Pandoc (Recommended for Technical Users)

```bash
# Install Pandoc (macOS)
brew install pandoc

# Convert Markdown to Word
pandoc 01-scope-of-work-template.md -o scope-of-work.docx

# Convert Markdown to PDF (requires LaTeX)
pandoc 01-scope-of-work-template.md -o scope-of-work.pdf
```

### Method 2: Online Converters

**Markdown to Word:**
- [Markdown to DOCX](https://cloudconvert.com/md-to-docx)
- [Dillinger](https://dillinger.io/) - Export to various formats

**Markdown to PDF:**
- [Markdown to PDF](https://www.markdowntopdf.com/)
- [MD2PDF](https://md2pdf.netlify.app/)

### Method 3: VS Code Extensions

If you use VS Code:
1. Install "Markdown PDF" extension
2. Open the .md file
3. Right-click  "Markdown PDF: Export (PDF)" or "(Word)"

### Method 4: Google Docs

1. Copy markdown content
2. Paste into Google Docs
3. Format as needed
4. Download as .docx or .pdf

### Method 5: Use HTML Templates

The `/templates-html/` folder contains styled HTML versions that:
- Look professional when printed
- Print directly to PDF
- Can be copied into Word

---

## Template Customization Guide

### Before Using Templates

1. **Replace Placeholders**
   - `[YOUR COMPANY]`  Your company name
   - `[CLIENT NAME]`  Client's name
   - `[DATE]`  Actual date
   - `$[X,XXX]`  Actual amounts

2. **Add Your Branding**
   - Logo (top of document)
   - Brand colors
   - Contact information
   - Website/social links

3. **Review Legal Terms**
   - Have attorney review contracts
   - Adjust for your jurisdiction
   - Add any required clauses

4. **Set Payment Details**
   - Bank information
   - Payment links
   - Accepted methods

---

## Quick Customization Checklist

```
 Replace all [PLACEHOLDERS]
 Add your company logo
 Update contact information
 Set your payment terms
 Review and adjust pricing tiers
 Have legal review contracts
 Test all payment links
 Save branded versions
```

---

## Template Categories

### Sales & Proposals
- `01-scope-of-work-template.md` - Detailed project definition
- `06-proposal-template.md` - Client-facing proposal
- `05-email-templates.md` - Sales communication

### Legal & Contracts
- `02-contract-template.md` - Service agreement
- `03-retainer-agreement-template.md` - Ongoing support

### Billing
- `04-invoice-templates.md` - All invoice types

### Delivery
- `07-project-brief-template.md` - Quick summary
- `08-handover-document-template.md` - Delivery docs

### Change Management
- `09-change-order-template.md` - Project scope modifications

---

## Tips for Professional Documents

1. **Consistency** - Use same fonts, colors, spacing
2. **White Space** - Don't crowd content
3. **Hierarchy** - Clear headings and sections
4. **Contact Info** - Always include how to reach you
5. **Version Control** - Date and version your documents

---

*See individual template files for full content.*
