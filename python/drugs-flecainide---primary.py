# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2024.

import sys, csv, re

codes = [{"code":"35520","system":"readv2"},{"code":"41735","system":"readv2"},{"code":"43501","system":"readv2"},{"code":"43502","system":"readv2"},{"code":"49434","system":"readv2"},{"code":"13549","system":"readv2"},{"code":"805","system":"readv2"},{"code":"56780","system":"readv2"},{"code":"30047","system":"readv2"},{"code":"32109","system":"readv2"},{"code":"51664","system":"readv2"},{"code":"56316","system":"readv2"},{"code":"7465","system":"readv2"},{"code":"49795","system":"readv2"},{"code":"10871","system":"readv2"},{"code":"14856","system":"readv2"},{"code":"1119","system":"readv2"},{"code":"30990","system":"readv2"},{"code":"34574","system":"readv2"},{"code":"34759","system":"readv2"},{"code":"43540","system":"readv2"},{"code":"40055","system":"readv2"},{"code":"31079","system":"readv2"},{"code":"49435","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drugs-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drugs-flecainide---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drugs-flecainide---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drugs-flecainide---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
