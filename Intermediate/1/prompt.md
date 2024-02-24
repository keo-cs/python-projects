# Python Intermediate Project #1

## File Hashes via VirusTotal API

Create a script that will help you investigate Hashes using OSINT found on VirusTotal. Your script should take in a hash value from the user. It should then send a request to the VirusTotal API and retrieve information about the hash. If the hash is not found, the script should clarify this.

If the hash is found, it should gather and display a menu with the following options:

- How many engines scanned this file
- What engines scanned this
- Conclusion from the different engines
- How many positive hits
- Look for keyword "ransom“
- Get input to look for other keywords

The user should be able to select one of the options and display the information. Because the public VT API is rate-limited (500 requests per day and rate of 4 requests per minute), you should implement a caching feature for your script. Before sending a request to the API, you should check your “cache” and see if you have grabbed the hash before.

You must make an account to receive an API key.
