import scrapy
from ..items import CareerviraItem
from scrapy.crawler import CrawlerProcess

class CareerviraSpider(scrapy.Spider):
    name = 'Careervira'
    start_urls =[
        'https://talentedge.com/iit-delhi/operations-management-and-analytics-course',
        'https://talentedge.com/xlri-jamshedpur/financial-management-course',
        'https://talentedge.com/iim-kozhikode/professional-certificate-program-marketing-sales-management-iim-kozhikode',
        'https://talentedge.com/iim-kozhikode/professional-certificate-programme-in-hr-management-and-analytics'
    ]

   

    def parse(self, response):
        items =CareerviraItem()
        all_div_quotes =response.css('div#app')

        for quotes in all_div_quotes:

            Title =quotes.css('.pl-title::text').extract()[0]+" -"+quotes.css('b::text').extract()[0]  
            ShortDescription =quotes.css('.desc_less p::text').extract()[0].split(".")[0]   
            Description=quotes.css(".desc p::text").extract()[0]      
            Keyskills =quotes.css(".key-skills-sec ul li ::text").extract()
            Prerequitsites =quotes.css('#deligibility li::text').extract()   

            #                                       ** Syllabus Section ** 
            
            
            # Element in Syllabus section 

            s=quotes.css('#dsyllabus a ::text').extract()
            Syllabus=[]

            for i in range(0,len(s)):
                sub =quotes.css(f'#syl-tab{i+1} li ::text').extract()
                Syllabus.append(s[i].split('\n')[2].strip())
                Syllabus.append(' | ')

            # Sub-Element in Syllabus Section
                if(len(sub)>0):                       
                    for j in range(0,len(sub)):
                        Syllabus.append(sub[j])
                    Syllabus.append(' || ')    
                else:
                    Syllabus.pop()
                    Syllabus.append(' || ')

            # Removing Last ||      
            Syllabus.pop()       



            #                                    ** price section - (INR +" "+Amount)  **

            
            b=quotes.css('.program-details-total-pay-amt-right::text').extract()
            final =b[0].split(' +\n')[0].strip()[0:3] +" "+b[0].split('\n')[1].split()[0]
            Price =final                                            
            

            items['Title'] =Title
            items['ShortDescription'] =ShortDescription
            items['Description'] =Description
            items['Keyskills'] =Keyskills
            items['Prerequitsites'] =Prerequitsites
            items['Syllabus'] =Syllabus
            items['Price'] =Price
           
            yield items


