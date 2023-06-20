

class HandlingOperator():
    '''
    Class for handling pricelist of all operators
    Also handling dial number to find the operator providing cheapest
    price for it

    Attributes:
        pricelists (dict): dictionary of operator associated with its own pricelist
        _dial_number (str): string of dialed number provided somewhere
        dial_prefixes (list): list of all prefixes extracted frrom dial number
    '''
    def __init__(self):
        self.pricelists = {}
        self._dial_number = ''
        self.dial_prefixes = []

    @property
    def dial_number(self):
        """
        The dial number property
        """
        return self._dial_number
    
    @dial_number.setter
    def dial_number(self, dial_):
        """
        Set dial number when receiving new dial number
        """
        self._dial_number = str(dial_)
        self.dial_prefixes = self.get_all_dial_prefixes()

    def get_all_dial_prefixes(self):
        """
        get list of all prefixes from dialed number
        
        Args:
            None

        Returns:
            list of all prefixes from dial number
        """
        ls = [self._dial_number[:i+1] for i in range(len(self._dial_number)-1)]
        ls.reverse()
        
        return ls

    def add_pricelist(self, pricelist):
        '''
        Add pricelist into dictionary of pricelists
        
        Args: 
            pricelist (str): a file of pricelist
        
        Returns:
            None
        '''
        d = self.load_pricelist_to_dict(pricelist)
        if pricelist not in self.pricelists:
            self.pricelists[pricelist] = d

    def load_pricelist_to_dict(self, pricelist):
        '''
        Load a file containing pricelist into dictionary
        
        Args: 
            pricelist (str): file name
        
        Returns:
            dictionary of key of prefix and value of price
        '''
        d = {}
        with open(pricelist) as f:
            for line in f:
                key, val = line.split()
                d[str(key)] = float(val)
        
        return d

    def find_cheapest_operator(self):
        '''
        Find the operator with the cheapest price for a given dial number

        Args:
            None

        Returns:
            name of operator providing the cheapest price for that dial number
        '''
        prices = {}
        for operator, pricelist in self.pricelists.items():
            for prefix in self.dial_prefixes:
                if prefix in pricelist:
                    prices[operator] = pricelist[prefix]
                    break

        if prices:
            return min(prices, key=prices.get)
        else:
            print('No operator with minimum price exist with number ', self._dial_number)
            return ''


if __name__ == "__main__":
    # Let's create the object of handling dial list here:
    handling = HandlingOperator()

    # If the pricelists are provided somewhere, let's add it into the handling
    pricelists = ['operator_A.txt', 'operator_B.txt']
    for list in pricelists:
        handling.add_pricelist(list)

    # Now, the dial number is provided somewhere:
    dial = '4673212345'
    handling.dial_number = dial
    
    # Find the operator providing the cheapest price:
    cheapest_operator = handling.find_cheapest_operator()
    assert cheapest_operator == 'operator_B.txt'
    print('operator with cheapest price is: ', cheapest_operator)


