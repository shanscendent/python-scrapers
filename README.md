# Python Scrapers
Collection of website scrapers.
Depends on:
- `requests`
- `bs4`
- `python-qbittorrent`

1. hliang-ctv - Scrapes Chinese TV magnets from hliang
   - hliang-tvbs-queen - Scrapes tvbs-queen magnets

## hliang-tvbs-queen
Scrapes tvbs-queen magnets from the hliang site and adds them to qbittorrent. 

### Installation
1. Requirements: `python3` and `pip`
2. `cd` to hliang-ctv folder
3. Run `quickstart.sh` to create a venv and install required packages.
4. Edit qbittorrent settings in `hliang-tvbs-queen.py` and absolute path to directory in `*cron.sh`
5. Add `*cron.sh` to crontab.

#### To-do
- Add logging to file