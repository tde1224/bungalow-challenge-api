from datetime import datetime
def clean(input, output, row):
    #sanitize input
    str_input = input.strip().lower()
    output = output.lower()
    toReturn = ""
    
    if output == "float":
        if str_input != "":
            try:
                toReturn = float(str_input)
            except:
                print('Error encountered on row ' + str(row) + ' while casting input to float for value:' + str_input + '\n')
        else:
                print('input was empty on row ' + str(row) + ', assigning proper type value for field')
                toReturn = 0.0
        return toReturn
    elif output == "integer":
        if str_input != "":
            str_input_dec = input.rstrip('0').rstrip('.') if '.' in input else input
            if not str_input_dec == "":
                try: 
                    input_int = int(str_input_dec)
                    toReturn = input_int
                except:
                    print('Error encountered on row ' + str(row) + ' while casting input to integer for value:' + str_input + ' input_int:' + input_int + '\n')
            else:
                toReturn = 0
        else:
                print('input was empty on row ' +  str(row) + ', assigning proper type value for field')
                toReturn = 0
        return toReturn
    elif output == "date":
        format_string = '%m/%d/%Y'
        try:
            toReturn = datetime.strptime(str_input, format_string).date()
        except:
            print('Error encountered on row ' +  str(row) + ' while constructing datetime object from string for value:' + str_input + '\n...Initializing empty datetime \n')
            toReturn = datetime.strptime('1/1/0001', format_string).date()
        return toReturn
    elif output == "price":
        if str_input != "":   
            try:            
                if "m" in str_input:
                    #store length of string
                    zeros = "000000"
                    length = (len(str_input) - 2)
                    if "." in str_input:
                        #Find number of decimal places
                        number_of_dec_places = len(str_input[str_input.index("."):length])
                        #trim zeros string to account for decimal places in input
                        zeros = zeros[number_of_dec_places - 1:]
                        #get numeric characters by trimming dollar sign and 'm' token off the input and adding string of zeros
                        num_characters = (str_input[1:length] + zeros).replace('.', '')
                    else:
                        num_characters = str_input[1:length]
                        number_of_digits = len(num_characters)
                        zeros = zeros[number_of_digits - 1:]
                        toReturn = num_characters + zeros
                elif "k" in str_input:
                    #store length of string
                    zeros = "000"
                    length = (len(str_input) - 2)
                    if "." in str_input:
                        #Find number of decimal places
                        number_of_dec_places = len(str_input[str_input.index("."):length])
                        #trim zeros string to account for decimal places in input
                        zeros = zeros[number_of_dec_places - 1:]
                        #get numeric characters by trimming dollar sign and 'm' token off the input and adding string of zeros
                        num_characters = (str_input[1:length] + zeros).replace('.', '')
                    else:
                        num_characters = str_input[1:length]
                        number_of_digits = len(num_characters)
                        zeros = zeros[number_of_digits - 1:]
                        toReturn = num_characters + zeros                     
                try:
                    toReturn = int(num_characters)
                except:
                    print('Error encountered on row ' +  str(row) + ' while casting input to price for value: ' + str_input + '\n')
            except ValueError:
                print('Error encountered on row ' +  str(row) + ' while parsing price for value: ' + str_input + '\n' + 'EXCEPTION: ' + Exception.value)
        else:
            print('input was empty on row ' +  str(row) + ', assigning proper type value for field')
            toReturn = 0
        return toReturn


