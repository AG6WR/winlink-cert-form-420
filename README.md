# Los Gatos / Monte Sereno CERT Form 420

Custom Winlink form for CERT (Community Emergency Response Team) incident reporting.

## Description

This is a custom Winlink Express form based on the Los Gatos / Monte Sereno CERT Form 420 - Incident Report. The form allows CERT volunteers to report incidents to the Incident Command Post (ICP), which can then be forwarded to the Emergency Operations Center (EOC).

## Files

- `CERT_Form_420.txt` - Template definition file (required by Winlink)
- `CERT_Form_420_Initial.html` - Editable form for filling out reports
- `CERT_Form_420_Viewer.html` - Read-only form for viewing received reports
- `cert_logo.png` - Los Gatos / Monte Sereno CERT logo
- `extract_logo.py` - Utility script to extract logo from PDF (development only)

## Version

**Version 2.5, 2023-04** (Latest update: November 2025)

Based on the official Los Gatos / Monte Sereno CERT Form 420 PDF.

### Recent Improvements (November 2025)

- **Added official CERT logo** extracted from original PDF
- Fixed radio button validation to properly check group selections
- Added ARIA labels and semantic HTML for improved accessibility
- Enhanced GPS error handling with detailed user feedback
- Added fieldset/legend structure for radio groups
- Fixed missing name attribute on "Incident Type Other" field
- Improved form validation to handle conditional required fields

## Features

- ✅ Responsive design (desktop, tablet, smartphone)
- ✅ Auto-generated Reference ID with override option
- ✅ GPS coordinates auto-detection with manual fallback
- ✅ Enhanced GPS error handling with detailed feedback
- ✅ Date/time auto-population for radio operators
- ✅ Interactive help tooltips for all fields
- ✅ Improved form validation with proper radio button group support
- ✅ Accessibility improvements (ARIA labels, semantic regions, fieldsets)
- ✅ Print-friendly viewer layout
- ✅ Compatible with Winlink Express

## Installation

1. Copy all three files to your Winlink Express Templates folder:
   - Windows: `C:\RMS Express\Templates\`
   - macOS/Linux: (varies by installation)

2. Restart Winlink Express

3. Create a new message and select "CERT Form 420" from the template list

## Workflow

1. **CERT Volunteer** fills out the "CERT Reporting Section" in the field
2. **ICP Staff** completes "ICP Operations Only" section with tracking and response info
3. **Radio Operators** complete tracking section
4. Form is transmitted via Winlink to EOC

## Field Identifiers

The form uses single-letter field identifiers (A-N) for easy voice/radio communication:

### ICP Operations Only
- **A** - Incident Reference ID
- **B** - Priority
- **C** - EOC Response Requested
- **D** - ICP Notes on Actions Plan
- **E** - Ham Records EOC ID

### CERT Reporting Section
- **F** - Your Name
- **G** - Team ID
- **H** - Incident Type
- **I** - Phone Number
- **J** - Site Access
- **K** - Incident Address
- **L** - Incident Description
- **M** - CERT Action Plan
- **N** - Notes

## Development

Built using:
- HTML5 with responsive CSS
- Vanilla JavaScript (ES5 for broad compatibility)
- Winlink variable system for data binding

## License

This form is provided for use by CERT teams and emergency response organizations.

## Credits

- Form design based on Los Gatos / Monte Sereno CERT Form 420
- Developed for Winlink Express compatibility
- Follows ICS (Incident Command System) form conventions

## Support

For issues or questions, please open a GitHub issue.

---

**73 de AG6WR**
