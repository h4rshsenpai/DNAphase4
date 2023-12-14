import re
import datetime

country_names = ['Andorra', 'Afghanistan', 'Antigua and Barbuda', 'Albania', 'Armenia', 'Angola', 'Argentina', 'Austria', 'Australia', 'Azerbaijan', 'Barbados', 'Bangladesh', 'Belgium', 'Burkina Faso', 'Bulgaria', 'Bahrain', 'Burundi', 'Benin', 'Brunei Darussalam', 'Bolivia', 'Brazil', 'Bahamas', 'Bhutan', 'Botswana', 'Belarus', 'Belize', 'Canada', 'Democratic Republic of the Congo', 'Republic of the Congo', "CÃ´te d'Ivoire", 'Chile', 'Cameroon', "China", 'Colombia', 'Costa Rica', 'Cuba', 'Cape Verde', 'Cyprus', 'Czech Republic', 'Germany', 'Djibouti', 'Denmark', 'Dominica', 'Dominican Republic', 'Ecuador', 'Estonia', 'Egypt', 'Eritrea', 'Ethiopia', 'Finland', 'Fiji', 'France', 'Gabon', 'Georgia', 'Ghana', 'The Gambia', 'Guinea', 'Greece', 'Guatemala', 'Haiti', 'Guinea-Bissau', 'Guyana', 'Honduras', 'Hungary', 'Indonesia', 'Republic of Ireland', 'Israel', 'India', 'Iraq', 'Iran', 'Iceland', 'Italy', 'Jamaica', 'Jordan', 'Japan', 'Kenya', 'Kyrgyzstan', 'Kiribati', 'North Korea', 'South Korea', 'Kuwait', 'Lebanon', 'Liechtenstein', 'Liberia', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Libya', 'Madagascar', 'Marshall Islands', 'Macedonia', 'Mali', 'Myanmar', 'Mongolia', 'Mauritania', 'Malta', 'Mauritius', 'Maldives', 'Malawi', 'Mexico', 'Malaysia', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Panama', 'Peru', 'Papua New Guinea', 'Philippines', 'Pakistan', 'Poland', 'Portugal', 'Palau', 'Paraguay', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saudi Arabia', 'Solomon Islands', 'Seychelles', 'Sudan', 'Sweden', 'Singapore', 'Slovenia', 'Slovakia', 'Sierra Leone', 'San Marino', 'Senegal', 'Somalia', 'Suriname', 'SÃ£o TomÃ© and PrÃ\xadncipe', 'Syria', 'Togo', 'Thailand', 'Tajikistan', 'Turkmenistan', 'Tunisia', 'Tonga', 'Turkey', 'Trinidad and Tobago', 'Tuvalu', 'Tanzania', 'Ukraine', 'Uganda', 'United States', 'Uruguay', 'Uzbekistan', 'Vatican City', 'Venezuela', 'Vietnam', 'Vanuatu', 'Yemen', 'Zambia', 'Zimbabwe', 'Algeria', 'Bosnia and Herzegovina', 'Cambodia', 'Central African Republic', 'Chad', 'Comoros', 'Croatia', 'East Timor', 'El Salvador', 'Equatorial Guinea', 'Grenada', 'Kazakhstan', 'Laos', 'Federated States of Micronesia', 'Moldova', 'Monaco', 'Montenegro', 'Morocco', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'Serbia', 'South Africa', 'Spain', 'Sri Lanka', 'Swaziland', 'Switzerland', 'United Arab Emirates', 'United Kingdom']

def ValidateNationality(name):
    name = name.strip()
    if name in country_names:
        return True 
    else:
        return False

def ValidateDate(datestring):
    datestring = datestring.strip()
    pattern = "^\d\d\d\d-\d\d-\d\d$"
    if bool(re.match(pattern, datestring)):
        year = int(datestring[0:4])
        month = int(datestring[5:7])
        day = int(datestring[8:10])
        if 1800 <= year <= datetime.datetime.now().year + 1:
            if 1 <= month <= 12:
                if 1 <= day <= 31:
                    return True
    return False


def ValidateSeasonYear(input):
  #  print(input)
    new_input = input.strip(' ')
    input = new_input
  #  print(input)
    length = len(input)
  #  print(length)
    if(length != 7):
        return False
    elif(length == 7):
        first = slice(0,2)
        new_one = input[first]
        second = slice(2,4)
        new_second = input[second]
        third = slice(4,5)
        new_third = input[third]
        fourth = slice(5,7)
        new_fourth = input[fourth]
        beg = 20
        convert_first = int(new_one)
        convert_second = int(new_second)
        convert_fourth = int(new_fourth)
        convert_third = input[third]
       # print(convert_first)
       # print(convert_second)
       # print(convert_fourth)
       # print()
        hyp = '-'
        if(convert_first == beg and convert_second == (convert_fourth-1) and hyp ==convert_third):
        #    print("here")
            return True
        else:
        #    print("not here")
            return False

def ValidatePositions(input):
    new_inp = input.replace(" ","")
  #  print(new_inp)
    if(new_inp.isalpha()):
        return True
    else:
        return False
