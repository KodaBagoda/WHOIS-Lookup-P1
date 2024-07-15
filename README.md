## WHOIS Lookup Tool (Python)

This Python script implements a simple WHOIS client to retrieve information about domain names using the WHOIS protocol.

**Features:**

- Performs WHOIS lookups for specified domain names.
- Connects to the IANA WHOIS server (`whois.iana.org`) by default.
- Handles potential socket errors and provides informative error messages.
- Decodes and presents the WHOIS response in a basic format.

**Dependencies:**

- This project requires no external libraries and uses only the built-in Python `socket` module.

**Usage:**

1. Clone this repository.
2. Open a terminal and navigate to the project directory.
3. Run the script using `python whois_lookup.py`.
4. The script will prompt you to enter a domain name (e.g., "example.com").
5. Upon successful lookup, the script will display the decoded WHOIS response.

**Example:**

```
Enter a domain name: example.com

Domain Name: example.com
Registrar Domain Name: EXAMPLE.COM
Registrar WHOIS Server: whois.verisign-ext.com
Registrar URL: https://www.verisign.com/whois/
Registrar IANA ID: 127
Registrar Abuse Contact Email: abuse@verisign.com
Registrar Abuse Contact Phone: +1-703-947-7644
... (truncated WHOIS response)
```

**Disclaimer:**

- The format and content of WHOIS responses can vary depending on the domain registrar and specific domain.
- This script provides a basic lookup functionality and may not display all available information from the WHOIS server.

**Contributing:**

Feel free to fork this repository and make improvements! Here are some ideas:

- Implement lookups against different WHOIS servers based on domain registries.
- Parse the WHOIS response to extract specific information (e.g., registrant contact details, creation date).
- Provide options to save the WHOIS response to a file.

**Security Considerations:**

- WHOIS information is publicly available, but scraping it aggressively can be considered unethical. Use this script responsibly and respect the terms of service of the WHOIS servers you connect to.
