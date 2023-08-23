



class Cline:

    def start(self)->None:
        print('='*50)

    def cityentry(self)->str:
        return input('Enter the city name to check for weather : ')

    def view_weather(self, wdata:dict)->None:
        print('\n\n\n')
        print('='*80)
        if wdata['location']['state'] == wdata['location']['city']:
            wdata['location'].pop('city')

        for data in wdata:
            if data=='location':
                for loc in wdata[data]:
                    print(f'|=  {loc:<28}-->   {str(wdata[data][loc]):<40}=|')
                continue
            print(f'|=  {data:<28}-->   {str(wdata[data]):<40}=|')
        print('='*80)
        