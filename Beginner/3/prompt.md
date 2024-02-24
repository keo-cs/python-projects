# Python Beginner Project #3

## URL Defang

Create a script that prompts the user to enter a potentially malicious URL, where in the script will remove & replace elements that would allow it’s use if clicked. This replacement should allow the URL to be easily readable. This script should then rest and await an additional URL entry.

* Example:
  * Input: `https://example.com/malicious/link`
  * Output: `hxxps[://]example[.]com/malicious/link`

**Bonus:** Use `Pyperclip` to send elements to users' clipboard.
