# Sending a finished result to AI Close

Read this only when a user who has a finished result from a skill asks to run the job across their team and wants the result sent with the request.

1. Save the finished result as a UTF-8 text file on the user's machine. A revised result gets a new file.
2. If the plugin is installed and a terminal is available, run this from the skill's directory, using the skill's name and real local paths:

   ```sh
   python3 ../../scripts/prepare_review.py SKILL-NAME RESULT.md review.html
   ```

3. Give the user the generated `review.html`. Opening it shows the result locally. Its labeled button sends that result to the review page only when the user clicks it. Never click it or submit it yourself.
4. If files or the script aren't available, give the user the skill's review link and tell them it carries the skill name only. Offer to save the result as a Markdown file they can choose on the review page. Say clearly that the page reads the file in their browser.

Never put work, names, email addresses or account details in a URL. Never upload work, schedule a meeting or submit a request for the user. If scheduling isn't available, leave the finished result with the user.
