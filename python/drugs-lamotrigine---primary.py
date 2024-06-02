# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2024.

import sys, csv, re

codes = [{"code":"4586","system":"readv2"},{"code":"51309","system":"readv2"},{"code":"6409","system":"readv2"},{"code":"59120","system":"readv2"},{"code":"56504","system":"readv2"},{"code":"7022","system":"readv2"},{"code":"50235","system":"readv2"},{"code":"39715","system":"readv2"},{"code":"61623","system":"readv2"},{"code":"39506","system":"readv2"},{"code":"47963","system":"readv2"},{"code":"32920","system":"readv2"},{"code":"10111","system":"readv2"},{"code":"2079","system":"readv2"},{"code":"19296","system":"readv2"},{"code":"47817","system":"readv2"},{"code":"49532","system":"readv2"},{"code":"15126","system":"readv2"},{"code":"59242","system":"readv2"},{"code":"55644","system":"readv2"},{"code":"2081","system":"readv2"},{"code":"59273","system":"readv2"},{"code":"48164","system":"readv2"},{"code":"46775","system":"readv2"},{"code":"60804","system":"readv2"},{"code":"60578","system":"readv2"},{"code":"59318","system":"readv2"},{"code":"59241","system":"readv2"},{"code":"16149","system":"readv2"},{"code":"3886","system":"readv2"},{"code":"48182","system":"readv2"},{"code":"61624","system":"readv2"},{"code":"7023","system":"readv2"},{"code":"39714","system":"readv2"},{"code":"29619","system":"readv2"},{"code":"57863","system":"readv2"},{"code":"35732","system":"readv2"},{"code":"59609","system":"readv2"},{"code":"60268","system":"readv2"},{"code":"5658","system":"readv2"},{"code":"29620","system":"readv2"},{"code":"51501","system":"readv2"},{"code":"5907","system":"readv2"},{"code":"45572","system":"readv2"},{"code":"60424","system":"readv2"},{"code":"61625","system":"readv2"},{"code":"5722","system":"readv2"},{"code":"5076","system":"readv2"},{"code":"11445","system":"readv2"},{"code":"59125","system":"readv2"},{"code":"54276","system":"readv2"},{"code":"2080","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drugs-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drugs-lamotrigine---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drugs-lamotrigine---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drugs-lamotrigine---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
