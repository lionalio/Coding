The program will receive one or more price lists in file of format:

prefix1  price1
prefix2 price2


The prefix of price list of any operator can be in any format for readability

However when entering the class, it should remove any non-digit characters and keep the digits only

Then, the class will guarantee that the formats of both prefixes in price lists and dialed number will always be the same

When there is any input of dialed number, the class will check the entire list of all prices for prefixes for all operators. It will choose the longest prefix for certain operator that match the prefix of dial numbers, then it will choose the minimum price(s) among them.

The minimum price for a certain dialed number might exist for more than one operator, so the output should be in a list

If no prefix exist for a certain dialed number, the result should be an empty list