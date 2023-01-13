import pdfplumber

# Open the PDF file
def filter_table(table):
    filtered = []
    for line in table:
        filtered.append([x for x in line if x is not None])
    return filtered

def extract_data(filtered, ITEM, MPN, QTY, NUP, DISCOUNT_AMOUNT):
    data = []
    for x in range(1,len(filtered)-3,4):
        data.append([filtered[x][ITEM],filtered[x][MPN],filtered[x][QTY],filtered[x][NUP],filtered[x][DISCOUNT_AMOUNT]])
        #print(data)
    return data

def JSON_CREATION(TEXT, DATA):
    JSON = []
    dict = {}
    TOPICS = ["Quote ID", "Start Date", "End Date"]
    TOPICS_2 = ["NAME", "Qty", "Net Buy Price","Cost Relief Price", "TEST"]
    for x in range(len(TEXT)):
        dict[TOPICS[x]] = TEXT[x]
    JSON.append(dict)
    dict = {}
    print(DATA)
    for y in range(len(DATA)):
        for x in range(len(DATA[y])):
            dict[TOPICS_2[x]] = DATA[y][x]
        JSON.append(dict)
        dict = {}



    print(JSON)



with pdfplumber.open("Quote.pdf") as pdf:
    
    # Get the first page
    page = pdf.pages[0]
    # Locate the table on the page
    table = page.extract_table()
    text = page.extract_text().split()
    QUOTE_ID = text[text.index("#:")+1]
    EXPIRATION = text[text.index("Expiration")+2]
    START = text[text.index("Start")+2]
    TEXT = [QUOTE_ID, EXPIRATION,START]

    print(QUOTE_ID, EXPIRATION, START)

    list = [x for x in table[0] if x is not None]
    filtered = filter_table(table)

    # Create an empty list to store the usernames
    username_column = []
    ITEM = filtered[0].index("Item")
    MPN = filtered[0].index("MPN")
    QTY = filtered[0].index("Qty")
    NUP = filtered[0].index("Net Unit Price")
    DISCOUNT_AMOUNT = filtered[2].index("Discount Amount")
    #print(ITEM, MPN,QTY,NUP,DISCOUNT_AMOUNT)
    DATA = extract_data(filtered, ITEM, MPN, QTY, NUP, DISCOUNT_AMOUNT)
    JSON_CREATION(TEXT, DATA)

    # Iterate through the rows of the table
    #for row in table:
        #print(row)
        # Append the value of the "username" column to the list
        # username_column.append(row[row.index("School")])


    #print(username_column)
