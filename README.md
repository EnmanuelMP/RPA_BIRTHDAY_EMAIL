# Birthday Reminder and Emailer

This Python program reminds you of birthdays stored in a CSV file and sends birthday emails using SMTP. It's a simple tool to automate birthday wishes to your contacts.

## Features

- Retrieves current day and month.
- Reads birthday data from a CSV file.
- Checks if there are any birthdays scheduled for today.
- Generates a random letter template and inserts the birthday person's name.
- Sends a birthday email using SMTP.

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/EnmanuelMP/RPA_BIRTHDAY_EMAIL.git
```

2. Install the required dependencies:

```bash
pip install pandas
```

3. Update the `birthdays.csv` file with your contacts' birthday data.

4. Modify the `MY_EMAIL` and `PASSWORD_TOKEN` variables in the script with your email credentials.

5. Customize the letter templates in the `letter_templates` directory according to your preference.

6. Run the program:

```bash
python birthday_reminder.py
```

## Usage

- Ensure that the `birthdays.csv` file is correctly formatted with columns `name`, `email`, `month`, and `day`.
- Letter templates should be plain text files in the `letter_templates` directory.
- Keep your email provider's SMTP settings updated in the script.
- Run the program daily to check for birthdays and send emails accordingly.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).