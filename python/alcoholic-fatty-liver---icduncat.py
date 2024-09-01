# phekb, 2024.

import sys, csv, re

codes = [{"code":"571","system":"icduncat"},{"code":"571.1","system":"icduncat"},{"code":"571.2","system":"icduncat"},{"code":"571.3","system":"icduncat"},{"code":"K70.x","system":"icduncat"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('alcoholic-fatty-liver-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["alcoholic-fatty-liver---icduncat-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["alcoholic-fatty-liver---icduncat-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["alcoholic-fatty-liver---icduncat-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
