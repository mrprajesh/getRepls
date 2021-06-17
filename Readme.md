# Aim
> In the absence of api/script to download the source code of repls ,
this script enables us to download the repls's via browser.

## Prerequisite

- Assumes the your are on admin role in the replit team
- and logged in into chrome/browser!

## How to run to download sources

We use this for downloading repls of CS1111 students in 2021.

- Step 0: Login to replit.com using your account.
- Step 1: Set the `projectName, teamsList`, and `rollNumbers`.
- Step 2: Run the below
```
python3 getRepls.py

```
- Step 3: Opens-up/Downloads a sequence repls sources as a `.zip` file.
- Step 4: You might have to click okay to download or gets downloaded in
your default download location if the repl URL is valid (not 404).

## Prereq
- Assuming downloaded `zip` files are present in `src` folder
- Assuming you have `moss` script+account and `chmod+ moss` in `src`
- Let's not add moss script publicly.

## How to run moss
- Step0: `cd src`
- Step1: Run the `run.sh`. // Extracts code in to folder with `rollNumber/rollNumber.c` i.e `rollNumber` is replit `username`
- Step2:  To run `moss -d cs*/*.c` -- all our rollNumbers start with `cs`


## Author

[Rajesh](mrprajesh.co.in)
