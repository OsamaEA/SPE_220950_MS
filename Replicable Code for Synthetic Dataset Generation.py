#!/usr/bin/env python
# coding: utf-8

'''
    START OF SCHEME FOR WORKFLOW
                        '''

# 1) Identify Drilling activities: during the past 23 years accroding to oil prices accounting for dollar inflation

# Identify dates of drilling for each well

# 2) Identify no. of entries: Assume number of entries into stock each year according to drilling activities - There is 
# assumption that number of POs every year or couple of years based on the drilling plan are [4,12], including drilling 
# and completion equipment. The number of entries is usually proportional to number of drilled wells - same PO could be 
# received on multiple times with different lead time due to urgency.

# Idnetify dates for stock entries according to number of entries. It will be totally randomized without restrictions
# for different categories. However, for the same category, there would be a gap of [1, 3] months at least between two entries

# 3) Identify no. of issuings: Assume number of issues for each drilled well is at least the following:
# A] 4 of (30 conductor - 24 conductor 20 casing - 13 casing - 9 casing - 7 casing - 5 casing) and maximum of #7 
#    - with couplings ranging between [5,20]
#    - with wellhead package for each casing (qty#1 wellhead and various qts. for valves and fittings)
#    - They should be issued in timeseries sequence
# B] X-overs are requested at once for all operations
# C] other items could be requested during drilling such as centralizers, shoes... etc.
# D] Tubing, completion equipment [5, 10], X-mas tree (qty#1 and various qts. for valves and fittings) are requested at once

# 4) Identify dates and no. of returns to stock: Assume that every category issued would be returned on 1-3 times to stock
# items return to stock withing 2 weeks to 3 months from issue date after being inspected.

# 5) Start populating items into each category
# A] Drilling Prep: 18 5/8" CSG - 20" CSG - 24" Conductor - 24" Drive pipe - 30" Conductor 
#    - Prep Accessories: Pad eyes for conductor - Wire slings - Drilling riser - 30" Drive Shoe - 30" Drive pipe
# B] Drilling Tubualr: 5" CSG - 7" CSG - 9 5/8" CSG - 13 3/8" CSG
#    - Tubualr Accessories: pup joints - couplings - crossovers
# C] Completion Tubular: 2 7/8" Tubing - 3 1/2" Tubing - 4 1/2" Tubing
#    - Completion Tubualar Accessories: 3 1/2" EUE riser - couplings - pup joints 5/8/12/15 ft - crossovers
# D] Completion Equipment: permanent packer, dual packer, retrievable pkr, x/f-nipple, xn/r nipple, SSD, WLEG, 
#                          flow coupling, perforate pup jt, blast jt, surge disk, (scsssv TR and WLR (landing nipple)
#                          , control line, buckles, straps, fittings), 
#                          (latches, redress kits), expansion joint, 
#    - Completion Accessories: surface crossover, pkr redress kit, permanent(sealbore extension - mill out extension 
#                              xover - locator - seal units - mule shoe guide), redress for SSD, KOT, 
# consumables: pulling/running tools for GLVs - KOT - spacer -

# E] Artificial lift: Gas lift (1.5/1 SPM,GLV/ orifice 1" and 1.5" different port sizes and dummy) - ESP

# F] Wellhead: Tubing head spool - CSG head spool - rings - 
# consumables: test plug - wear bushing - 
# Accessories: studs - nuts - sleeve seals

# G) Xmas Tree: Signle block - dual single block - tubing hanger - adaptor assembly - 
# Accessories: studs - nuts - sleeve seals - SBMS - ring gasket - 

# chokes fixed different size and adjustable /flanges / plugs for chokes for wells on production - o rings - studs - nuts
# tree cap - 

#at the start of drilling, 1-3 issues are prepared for the well
#within three months of drilling, at least 4-7 issues of drilling tubular
#within three months of drilling, at least 2-3 issues of drilling wellhead
#after the last order and within 7 days to 14 days, issue 1-2 completion orders and 1 wellhead stack


'''
    END OF SCHEME FOR WORKFLOW
                        '''


years_dict = {2000: np.nan, 2001: np.nan, 2002: np.nan, 2003: np.nan, 2004: np.nan, 2005: np.nan, 2006: np.nan,
                         2007: np.nan, 2008: np.nan, 2009: np.nan, 2010: np.nan, 2011: np.nan, 2012: np.nan, 2013: np.nan,
                         2014: np.nan, 2015: np.nan, 2016: np.nan, 2017: np.nan, 2018: np.nan, 2019: np.nan, 2020: np.nan,
                         2021: np.nan, 2022: np.nan, 2023: np.nan}

main_inventory_entries = ['Drilling Tubular - reception', 'Completion Tubular - reception',
                          'Completion Equipment - reception', 'Completion Artificial Lift - reception',
                          'Wellhead - reception', 'Wellhead Xmass Tree - reception']
entries_weights = [0.10, 0.10, 0.50, 0.10, 0.10, 0.10] #weights are favored as 2-2-6, however wellhead and tubualr are already
# divided into two categories, hence it is kept as 1. However, completion equipment are a lot and enter the stock on more frequencies

# Define subclasses of each category list
casing_tubular_list = ['5" CSG', '7" CSG', '9 5/8" CSG', '13 3/8" CSG']
conductor_tubular_list = ['18 5/8" CSG', '20" CSG', '24" Conductor', '30" Conductor']
drilling_tubular_list = ['5" CSG', '7" CSG', '9 5/8" CSG', '13 3/8" CSG',
                         '18 5/8" CSG', '20" CSG', '24" Conductor', '30" Conductor']
completion_tubular_list = ['2 7/8" Tubing', '3 1/2" Tubing', '4 1/2" Tubing']
completion_equipment_list = ['permanent packer', 'dual packer', 'retrievable pkr', 'sealbore packer', 'top no-go nipple',
                   'bottom no-go-nipple', 'SSD', 'WLEG', 'flow coupling', 'perforated pup joint', 'blast joint',
                   'surge disk', 'TRSCSSSV', 'WLSCSSSV', 'landing nipple', 'expansion joint', 'sand screens']
completion_artificial_lift_list = ['gas lift', 'ESP', 'jet pump']
wellhead_list = []
wellhead_xmass_tree_list = []
inventory_material = drilling_tubular_list + completion_tubular_list + completion_equipment_list + completion_equipment_list


years_dict = {2000: np.nan, 2001: np.nan, 2002: np.nan, 2003: np.nan, 2004: np.nan, 2005: np.nan, 2006: np.nan,
                         2007: np.nan, 2008: np.nan, 2009: np.nan, 2010: np.nan, 2011: np.nan, 2012: np.nan, 2013: np.nan,
                         2014: np.nan, 2015: np.nan, 2016: np.nan, 2017: np.nan, 2018: np.nan, 2019: np.nan, 2020: np.nan,
                         2021: np.nan, 2022: np.nan, 2023: np.nan}

main_inventory_entries = ['Drilling Tubular - reception', 'Completion Tubular - reception',
                          'Completion Equipment - reception', 'Completion Artificial Lift - reception',
                          'Wellhead - reception', 'Wellhead Xmass Tree - reception']
entries_weights = [0.10, 0.10, 0.50, 0.10, 0.10, 0.10] #weights are favored as 2-2-6, however wellhead and tubualr are already
# divided into two categories, hence it is kept as 1. However, completion equipment are a lot and enter the stock on more frequencies

# Define subclasses of each category list
casing_tubular_list = ['5" CSG', '7" CSG', '9 5/8" CSG', '13 3/8" CSG']
conductor_tubular_list = ['18 5/8" CSG', '20" CSG', '24" Conductor', '30" Conductor']
drilling_tubular_list = ['5" CSG', '7" CSG', '9 5/8" CSG', '13 3/8" CSG',
                         '18 5/8" CSG', '20" CSG', '24" Conductor', '30" Conductor']
completion_tubular_list = ['2 7/8" Tubing', '3 1/2" Tubing', '4 1/2" Tubing']
completion_equipment_list = ['9 5/8 in permanent packer', '9 5/8 in dual packer', '9 5/8 in retrievable pkr', 
                             '9 5/8 in sealbore packer', '4 1/2 in top no-go nipple',
                   '4 1/2 in bottom no-go-nipple', '4 1/2 in SSD', '4 1/2 in WLEG', '4 1/2 in flow coupling', 
                             '4 1/2 in perforated pup joint', '4 1/2 in blast joint',
                   '4 1/2 in surge disk', '4 1/2 in TRSCSSSV', '4 1/2 in WLSCSSSV', '4 1/2 in landing nipple', 
                             '4 1/2 in expansion joint', '4 in sand screens', '4 1/2 in tubing anchor',
                    '4 1/2 in flow control device', '4 1/2 in check valve', 'control line', '9 5/8 in feedthru packer',
                             
                            '7 in permanent packer', '7 in dual packer', '7 in retrievable pkr', 
                             '7 in sealbore packer', '3 1/2 in top no-go nipple',
                   '3 1/2 in bottom no-go-nipple', '3 1/2 in SSD', '3 1/2 in WLEG', '3 1/2 in flow coupling', 
                             '3 1/2 in perforated pup joint', '3 1/2 in blast joint',
                   '3 1/2 in surge disk', '3 1/2 in TRSCSSSV', '3 1/2 in WLSCSSSV', '3 1/2 in landing nipple', 
                             '3 1/2 in expansion joint', '3 1/2 in sand screens', '3 1/2 in tubing anchor',
                    '3 1/2 in flow control device', '3 1/2 in check valve', 'control line', '7 in feedthru packer',
                            
                             '2 7/8 in top no-go nipple',
                   '2 7/8 in bottom no-go-nipple', '2 7/8 in SSD', '2 7/8 in WLEG', '2 7/8 in flow coupling', 
                             '2 7/8 in perforated pup joint', '2 7/8 in blast joint',
                   '2 7/8 in surge disk', '2 7/8 in TRSCSSSV', '2 7/8 in WLSCSSSV', '2 7/8 in landing nipple', 
                             '2 7/8 in expansion joint', '2 7/8 in sand screens', '2 7/8 in tubing anchor',
                    '2 7/8 in flow control device', '2 7/8 in check valve', 'control line']

completion_artificial_lift_list = ['gas lift IPO 1.5', 'gas lift IPO 1', 'gas lift PPO 1.5', 'gas lift PPO 1',
                                   'gas lift ddummy valve', 'gas lift chemicacl injection valve', 'gas lift circulation valve',
                                   'gas lift SPM 1.5', 'gas lift SPM 1', 
                                   'ESP motor', 'ESP pump', 'ESP intake section', 'ESP seal section', 'ESP power cable', 
                                   'ESP motor lead extension', 'ESP gas separator', 'downhole sensor''ESP', 'jet pump']
wellhead_list = []
wellhead_xmass_tree_list = []
inventory_material = drilling_tubular_list + completion_tubular_list + completion_equipment_list + completion_equipment_list

def drilling_activities():
    '''
        This function is used to calculate oil prices accounting for inflation rate from year 2000
        OUTPUT:
            Dictionary of Year and corresoponding number of wells to be drilled every year by a major exploration company
                                                                                                                        '''
    global years_dict
    np.random.seed(42)
    # average yearly oil prices
    yearly_oil_prices = {2000: 30.38, 2001: 25.98, 2002: 26.19, 2003: 31.08, 2004: 41.51, 2005: 56.64, 2006: 66.05,
                         2007: 72.34, 2008: 99.67, 2009: 61.95, 2010: 79.48, 2011: 94.88, 2012: 94.05, 2013: 97.98,
                         2014: 93.17, 2015: 48.66, 2016: 43.29, 2017: 50.80, 2018: 65.23, 2019: 56.99, 2020: 39.68,
                         2021: 68.17, 2022: 94.53, 2023: 77.72}

    # average calculated dollar inflation rate
    dollar_infation_rate = {2000: 78.30, 2001: 73.50, 2002: 70.70, 2003: 66.90, 2004: 62.50, 2005: 57.20, 2006: 52.30,
                         2007: 48.10, 2008: 42.60, 2009: 43.10, 2010: 40.80, 2011: 36.50, 2012: 33.70, 2013: 31.80,
                         2014: 29.70, 2015: 29.50, 2016: 27.90, 2017: 25.30, 2018: 22.30, 2019: 20.10, 2020: 18.60,
                         2021: 13.30, 2022: 4.90, 2023: 0.00}
    
    # calculating the inflated oil prices
    inflated_oil_prices = [round(yearly_oil_prices[year] * (1+ dollar_infation_rate[year]/100), 2) for year in yearly_oil_prices]
    
    # number of wells to be drilled by an exploration company on yearly basis
    drilled_wells =  [round(price/10) for price in inflated_oil_prices]
    
    yearly_drilled_wells = years_dict.copy() #empty dictionary
    for i, year in enumerate(years_dict):
        yearly_drilled_wells[year] = drilled_wells[i]
   
    return(yearly_drilled_wells)


def generate_drilling_dates(yearly_drilling = drilling_activities()):
    '''
        This function is used to generate dates of drilling wells
        INPUTS:
                yearly_drilling: dictionary of number of drilled wells a year
        OUTPUT: 
                Dictionary for dates of drilling
                                                                                                    '''
    np.random.seed(42)
    drilling_dates = [] #initiate a list of drilling dates
    for year, number_of_wells in yearly_drilling.items():
        random_day = np.random.randint(0,365, number_of_wells) #generate a random number of days during a year for n times
        first_day_of_year = datetime(year, 1, 1) #initalize first day of the corresponding year
        yearly_dates = [first_day_of_year + timedelta(day) for day in random_day.tolist()] #list of entries dates in year of interest
        drilling_dates.extend(yearly_dates) #append entry date
        
    drilling_dates = sorted(drilling_dates)
    return(drilling_dates)

dates = generate_drilling_dates()

def yearly_entries(avg_entries = 20, std_entries = 6, min_entries = 10, max_entries = 30):
    '''
        This function is used to identify number of POs received every year according to drilling activities
        INPUT:
            avg_entries: average number of POs expected
            std_entries: standard deviation of POs expected
            min_entries: minimum number of POs a year
            max_entries: maximum number of POs a year
        OUTPUT:
            distributed_POs: dictionary of number of entries expected a year
                                                                                                                    '''
    global years_dict
    np.random.seed(42)
    mean_drilling_activites = np.mean(list(drilling_activities().values()))
    # make scaling factor varying for each iteration in the comprehension list
    POs_list = [value*(np.random.normal(avg_entries, std_entries)/mean_drilling_activites) for value in drilling_activities().values()] # new PO list
    distributed_POs = np.round(np.random.poisson(POs_list), 0) #poisson distribution to follow simialr trend                       

    yearly_entries = years_dict.copy() #empty dictionary
    # Assign POs to each year
    for i, year in enumerate(years_dict):
        if distributed_POs[i] < min_entries: #minimum number of three transactions a year
            yearly_entries[year] = int(np.random.uniform(min_entries,min_entries+std_entries)) #tolerance of 3
        elif distributed_POs[i] > max_entries: #maximum number of 12 transactions a year
            yearly_entries[year] = int(np.random.uniform(max_entries-std_entries,max_entries)) #tolerance of 3
        else:
            yearly_entries[year] = distributed_POs[i]
    
    return(yearly_entries)

def generate_entries_dates(entries_transactions = yearly_entries()):
    '''
        This function is used to generate dates of entry transactions into the inventory system
        INPUTS:
                entries_transactions: dictionary of number of entries expected a year
        OUTPUT: 
                Dictionary for dates and category of transaction
                                                                                                    '''
    global main_inventory_entries, entries_weights
    np.random.seed(42)
    entries_dates = [] #initiate a list of entries dates
    entries_type = [] #initiate a list of entries types
    for year, entries in entries_transactions.items():
        random_day = np.random.randint(0,365, entries) #generate a random number of days during a year for n times
        first_day_of_year = datetime(year, 1, 1) #initalize first day of the corresponding year
        yearly_dates = [first_day_of_year + timedelta(day) for day in random_day.tolist()] #list of entries dates in year of interest
        entries_dates.extend(yearly_dates) #append entry date
        
        while True: #while loop to make sure that each category of entry exists at least once and at maximum five times
            random_type = np.random.choice(main_inventory_entries, entries, 
                                           p = entries_weights, replace = True) #select random inventory type with replacement
            min_once_condition = all(cat in random_type for cat in main_inventory_entries)
            max_five_condition = all([val <= 6 for val in list(Counter(random_type).values())])
            if (min_once_condition and max_five_condition):
                break
        entries_type.extend(random_type) #append entry type
    entries_categories = dict(zip(entries_dates, entries_type)) #initialize a dictionary of entries dates and equipment
    return(entries_categories)

counted_entries = Counter(generate_entries_dates().values()) #number of entries for each category in inventory

years = [date.year for date in list(generate_entries_dates().keys())] #years of receptions
cats = list(generate_entries_dates().values()) #categories as a list
unique_years, unique_cats = sorted(set(years)), sorted(set(cats)) #unique years and categories
counts = Counter(list(zip(years, cats))) #counting each year against category
count_matrix = [[counts[(year, cat)] for cat in unique_cats] for year in unique_years] #count of each category as sorted


def generate_issue_return_transactions(drilling_activities = generate_drilling_dates()):
    '''
        This function is used to generate a dictionary that shows issue and return dates and types
        INPUT:
            drilling_activities: dates of drilling activities
        OUTPUTL
            Two lists of issue and return transactions dates and types'''
    
    description_issue = []
    date_issue = []
    description_return = []
    date_return = []
    issue_return_dates = []
    description_issue_return = []
    np.random.seed(42)
    
    #########################################################
    def description(description_list, transactions_num, category, prefix):
        '''
            This sub function is used to generate description of each issue and its number for a well
            INPUT:
                description_list: description list whether issue or return
                transactions_num: number of transactions
                category: string whether issue or return
                prefix: string of the name of category
                                                                                                        '''
        nonlocal i
        for _ in range(transactions_num):
            cat_description = 'well#{} - {} - {}#{}'.format(i+1, category, prefix, _+1) #description of issue section
            description_list.append(cat_description) #appending to non local yet non global list
    ##########################################################
            
        
    for i, drilling_date in enumerate(drilling_activities):
        # identify number of necessary issues for each well [tubular - completion equipment - wellhead]
        # 1) Conductor section
        drilling_prep_issues = np.random.randint(1, 4) #at the start of drilling, 1-3 issues are prepared for the well, for conductors
        drilling_prep_days = np.random.randint(0,15, drilling_prep_issues) #items are issued within 14 days from RIG move to location
        drilling_prep_dates = sorted([drilling_date + timedelta(day) for day in drilling_prep_days.tolist()]) #prep issue dates
        last_prep_date = drilling_prep_dates[-1] #last preparation equipment sent to RIG location
        date_issue.extend(drilling_prep_dates)
        description(description_issue, drilling_prep_issues, 'issue', 'drilling prep tubular')
        # return section
        drilling_prep_returns = np.random.randint(max(1, drilling_prep_issues - 2), drilling_prep_issues+1) #return on one to three times
        drilling_prep_return_dates = sorted([last_prep_date + timedelta(day) for day in #return date within 2 weeks to 3 months
                                      (np.random.randint(15, 90, drilling_prep_returns)).tolist()]) 
        date_return.extend(drilling_prep_return_dates) #append to list only one return transaction
        description(description_return, drilling_prep_returns, 'return', 'drilling prep tubular')
        ######################################################

        # 2) Casing and liner section
        drilling_tubular_issues = np.random.randint(2,6) #while drilling, at least 2-6 issues of drilling tubular
        drilling_tubualr_days = np.random.randint(15,90, drilling_tubular_issues) #items are issued within 0.5-3 months from drilling
        drilling_tubular_dates = sorted([last_prep_date + timedelta(day) for day in drilling_tubualr_days.tolist()]) #prep issue dates
        last_drilling_tubular_date = drilling_tubular_dates[-1] #last drilling operation on well
        date_issue.extend(drilling_tubular_dates)
        description(description_issue, drilling_tubular_issues, 'issue', 'drilling tubular')
        # return section
        drilling_tubular_returns = np.random.randint(max(1, drilling_tubular_issues - 2), drilling_tubular_issues+1) #return on one to three times
        drilling_tubular_return_dates = sorted([last_drilling_tubular_date + timedelta(day) for day in #return date within 2 weeks to 3 months
                                      (np.random.randint(15, 90, drilling_tubular_returns)).tolist()]) 
        date_return.extend(drilling_tubular_return_dates) #append to list only one return transaction
        description(description_return, drilling_tubular_returns, 'return', 'drilling tubular')
        ######################################################        

        # 3) wellhead for each size section
        drilling_wellhead_issues = drilling_tubular_issues
        drilling_wellhead_days = np.random.randint(-7,7, drilling_wellhead_issues) #items are issued within +/- 7 days from tubular section
        # adding each date of tubular with wellhead number of days to issue on location
        drilling_wellhead_dates = [tubular_date + timedelta(wellhead_day) for 
                                   tubular_date, wellhead_day in zip(drilling_tubular_dates, drilling_wellhead_days.tolist())]
        date_issue.extend(drilling_wellhead_dates)
        description(description_issue, drilling_wellhead_issues, 'issue', 'drilling wellhead')
        last_wellhead_date = drilling_wellhead_dates[-1] #last issue
        # return section
        drilling_wellhead_returns = np.random.randint(max(1, drilling_wellhead_issues - 2), drilling_wellhead_issues+1) #return on one to three times
        drilling_wellhead_return_dates = sorted([last_wellhead_date + timedelta(day) for day in #return date within 2 weeks to 3 months
                                      (np.random.randint(15, 90, drilling_wellhead_returns)).tolist()]) 
        date_return.extend(drilling_wellhead_return_dates) #append to list only one return transaction
        description(description_return, drilling_wellhead_returns, 'return', 'drilling wellhead')
        ######################################################
        
        # 4) completion tubing section
        completion_tubular_issues = np.random.randint(1, 3)#after drilling, completion tubular are ordered once or twice if requested
        completion_tubular_days = np.random.randint(3,14, completion_tubular_issues) #items are issued within 14 days from last section
        completion_tubular_dates = sorted([last_drilling_tubular_date + timedelta(day) for day in completion_tubular_days.tolist()]) #prep issue dates
        first_completion_issue_date = completion_tubular_dates[0]
        date_issue.extend(completion_tubular_dates)
        description(description_issue, completion_tubular_issues, 'issue', 'completion tubular')
        # return section
        completion_tubular_returns = np.random.randint(max(1, completion_tubular_issues - 2), completion_tubular_issues+1) #return on one to three times
        completion_tubular_return_dates = sorted([first_completion_issue_date + timedelta(day) for day in #return date within 2 weeks to 3 months
                                      (np.random.randint(15, 90, completion_tubular_returns)).tolist()]) 
        date_return.extend(completion_tubular_return_dates) #append to list only one return transaction
        description(description_return, completion_tubular_returns, 'return', 'completion tubular')
        ######################################################        
        
        # 5) completion accessories section
        completion_material_issues = np.random.randint(1, 3)#after drilling, completion equipment are ordered on single to three times
        completion_material_days = np.random.randint(-3,10, completion_material_issues) #items are issued within -3 to 10 days days from tubular issue
        completion_material_dates = sorted([first_completion_issue_date + timedelta(day) for day in completion_material_days.tolist()]) #prep issue dates
        date_issue.extend(completion_material_dates)
        description(description_issue, completion_material_issues, 'issue', 'completion equipment')
        last_completion_material_date = completion_material_dates[-1]
        # return section
        completion_material_returns = np.random.randint(max(1, completion_material_issues - 2), completion_material_issues+1) #return on one to three times
        completion_material_return_dates = sorted([last_completion_material_date + timedelta(day) for day in #return date within 2 weeks to 3 months
                                      (np.random.randint(15, 90, completion_material_returns)).tolist()]) 
        date_return.extend(completion_material_return_dates) #append to list only one return transaction
        description(description_return, completion_material_returns, 'return', 'completion equipment')
        ######################################################        
        
        # 6) xmass tree section
        xmass_tree_wellhead_issues = np.random.randint(1, 3)#after drilling, xmass tree could be delivered twice for backup
        xmass_tree_wellhead_day = np.random.randint(-3,5, xmass_tree_wellhead_issues) #items are issued within -3 to 5 days from tubular issue
        xmass_tree_wellhead_dates = sorted([first_completion_issue_date + timedelta(day) for day in xmass_tree_wellhead_day.tolist()]) #prep issue dates
        date_issue.extend(xmass_tree_wellhead_dates)
        description(description_issue, xmass_tree_wellhead_issues, 'issue', 'wellhead xmass tree')
        last_wellhead_xmass_tree_date = xmass_tree_wellhead_dates[-1]
        # return section
        wellhead_xmass_tree_returns = np.random.randint(max(1, xmass_tree_wellhead_issues - 2), xmass_tree_wellhead_issues+1) #return on one to three times
        wellhead_xmass_tree_return_dates = sorted([last_wellhead_xmass_tree_date + timedelta(day) for day in #return date within 2 weeks to 3 months
                                      (np.random.randint(15, 90, wellhead_xmass_tree_returns)).tolist()]) 
        date_return.extend(wellhead_xmass_tree_return_dates) #append to list only one return transaction
        description(description_return, wellhead_xmass_tree_returns, 'return', 'wellhead xmass tree')
        ######################################################

    # append issue and return lists together and convert them into a dataframe for better readability
    issue_return_dates.extend(date_issue), issue_return_dates.extend(date_return)
    description_issue_return.extend(description_issue), description_issue_return.extend(description_return)

    
    return(issue_return_dates, description_issue_return)


def preprocess_issue_return_data(dates = generate_issue_return_transactions()[0], 
                                 transaction_description = generate_issue_return_transactions()[1]):
    '''
        This function take dates and types of transactions as inputs and output a clean dataset
                                                                                                '''
    # generate dataframe with dates and types of transactions with full description
    pre_df = pd.DataFrame([dates, transaction_description], 
                                      index = ['transaction_date', 'transaction_type']).T
    # split description into multiple columns according to well name, transaction type, and category of operation
    pre_df[['well', 'transaction', 'transaction_category']] = pre_df['transaction_type'].str.split('-', expand = True, n = 2)
    for col in pre_df.select_dtypes(include='object').columns: #strip columns that contain string only and avoid datetime column
        pre_df[col] = pre_df[col].str.strip()
    pre_df.drop(['transaction_type'], axis = 1, inplace = True) # drop the splitted column
    return(pre_df)

issue_return_df = preprocess_issue_return_data()

def generate_stock_items(main_list, max_value = 10):
    '''
        This function is used to generate diverse items with different specs for each subclass of stock categories
        INPUTS:
            main_list: list of the main inventory category such as tubular or completion... etc
            list_description: category of the item upon which the maximum and minimum are identified
        OUTPUT:
            list of all possible subclasses
                                                                                                                    '''
    #np.random.seed(42)
    subclasses = [] #initiate an empty list for sub classes

    for item in main_list:
        left_skewed_numbers = np.random.exponential(scale=1, size=10) #generate left skewed exponential distribution
        #pick a random number that is bounded between min and max values required
        #random_number = int(np.random.choice(min_value + left_skewed_numbers * (max_value - min_value) / left_skewed_numbers.max()))
        subclasses.extend([f"{item} - spec#{i}" for i in range(1, max_value + 1)]) #generate names for subclasses
            
    return(subclasses)

def show_stock_entries_status(entries = generate_entries_dates()):
    '''
        This function is used to output a dataframe showing the status of stock entries displaying total length of dates and items.
        It has two nested functions that assist in the code.
        INPUT:
            entries: dictornary of dates and reception/entries transactions
        OUTPUT:
            a datframe that shows all dates and subclass transaction for each category
                                                                                                            '''
    
    np.random.seed(42)
    ###########################################################################
    # Local function to sort entries
    def get_sorted_entries(entries, category):
        '''
            This local function is used to sort entries of each category by date
            INPUTS:
                entries: dates of reception activities
                category: string of reception category
            OUTPUT:
                sorted list of entry dates for each category
                                                                                                            '''
        return sorted([key for key, value in entries.items() if value == category])
    ###########################################################################

    drilling_tubualr_entries = get_sorted_entries(entries, 'Drilling Tubular - reception')
    completion_tubualr_entries = get_sorted_entries(entries, 'Completion Tubular - reception')
    completion_equipment_entries = get_sorted_entries(entries, 'Completion Equipment - reception')
    completion_artificial_lift_entries = get_sorted_entries(entries, 'Completion Artificial Lift - reception')
    wellhead_entries = get_sorted_entries(entries, 'Wellhead - reception')
    wellhead_xmass_tree_entries = get_sorted_entries(entries, 'Wellhead Xmass Tree - reception')

    # Identify subclasses for each category
    drilling_tubualr_subclasses = generate_stock_items(drilling_tubular_list)
    completion_tubular_subclasses = generate_stock_items(completion_tubular_list)
    completion_equipment_subclasses = generate_stock_items(completion_equipment_list)
    completion_artificial_lift_subclasses = generate_stock_items(completion_artificial_lift_list)
    wellhead_subclasses = generate_stock_items(wellhead_list)
    wellhead_xmass_tree_subclasses = generate_stock_items(wellhead_xmass_tree_list)

    # list of lists that includes all sub classes
    subclass_list = [drilling_tubualr_subclasses, completion_tubular_subclasses, completion_equipment_subclasses,
                     completion_artificial_lift_subclasses]#, wellhead_subclasses, wellhead_xmass_tree_subclasses]
    subentrydate_list = [drilling_tubualr_entries, completion_tubualr_entries, completion_equipment_entries,
                     completion_artificial_lift_entries]#, wellhead_entries, wellhead_xmass_tree_entries]    
    print(
          f'There are diverse subclasses of main categories items as below: \n\
          {len(drilling_tubualr_subclasses)} for drilling tubualr received in {len(drilling_tubualr_entries)} dates \n\
          {len(completion_tubular_subclasses)} for completion tubualr received in {len(completion_tubualr_entries)} dates \n\
          {len(completion_equipment_subclasses)} for completion equipment received in {len(completion_equipment_entries)} dates \n\
          {len(completion_artificial_lift_subclasses)} for completion artificial lift received in {len(completion_artificial_lift_entries)} dates \n\
          {len(wellhead_subclasses)} for wellhead received in {len(wellhead_entries)} dates \n\
          {len(wellhead_xmass_tree_subclasses)} for wellhead xmass tree received in {len(wellhead_xmass_tree_entries)} dates \n\
          ') 
    
    ###########################################################################    
    def generate_sub_classes_entries():
        '''
            This function is used to generate the type or subclass of main items and the corresponding date that it enters the
            inventory at. It is a nested function, so that the necessary variables are loaded as nonlocals
            OUTPUT:
                a dataframe that contains reception transactions for all items categorized and dated accordingly
                                                                                                                            '''
        nonlocal subclass_list, subentrydate_list
        # LOGIC is:
        # iterate through date and subclass of each transaction of the main category subclasses dates
        # iterate through the main category entry dates. Select random number of items to enter the stock at each date between zero and
        # the maximum number of items in a category. Pick random unique items with replacement according to random number n.
        # for each selected unique item, pick one description of the corresponding descriptions to it and add it to list.
        # finally show a dataframe that shows each transaction, wtih the corresponding transaction subclass
        
        
        #identify obsolete dates for each item
        flattened_list = [item for sublist in subclass_list for item in sublist] #flatten list as 1D
        # Last year of transaction year for each item after which the item is assumed obsolete
        obsolete_years = [np.random.randint(2000, 2024) if random.choices(['Working', 'Obsolete'], weights = [0.15, 0.85])
                          [0] == 'Obsolete' else 2024 for _ in range(len([item for sublist in flattened_list for item in sublist]))]
        
        full_data_list = []      
        ___ = [] #temporary list that would include all subclasses to assist in weight assigning
        for full_subclass, subentrydate in zip(subclass_list, subentrydate_list):
            #print(full_subclass)
            sub_list_df = []
            unique_items = set([item.split('-')[0] for item in full_subclass]) #unique main item in each category ignoring description
            for date in subentrydate: #for each date in entries in each year covering yearly drilled wells
                random_entry_items_num = np.random.randint(len(unique_items) + 1) #select number of entries #it could be zero up to unique items
                entry_items = np.random.choice(list(unique_items), random_entry_items_num, replace = True) #select unique items for n times
                #print(date, '---------------')
                date_year = date.year
                split_one = np.random.choice([2002,2003,2004])
                split_two = np.random.choice([2007,2008,2009])
                split_three = np.random.choice([2012,2013,2014])
                split_four = np.random.choice([2017,2018,2019])       
                max_num = [2 if date_year < split_one else 4 if date_year < split_two else 
                           6 if date_year < split_three else 8 if date_year < split_four else 10][0]
                subclass = [sub for sub in full_subclass if int(sub.split('#')[1]) <= np.random.randint(2, max_num+1)]
                #wts = np.array([[1,1] if date_year < split_one else [1, 1, 2, 2] if date_year < split_two else 
                #               [1,1,2,2,3,3] if date_year < split_three else [1,1,2,2,3,3,4,4] if date_year < split_four else
                #               [1,1,2,2,3,3,4,4,5,5]])[0]
                #print(subclass)
                sub_class_item_list = []
                #print(max_num, subclass)
                for _ in entry_items: #for every unique item
                    #print(_)
                    sub_unique_items_all = [item for item in subclass if _ in item] #subclasses of unique items
                    sub_unique_items = [item for item in sub_unique_items_all if date_year < obsolete_years[flattened_list.index(item)]]
                    
                    #print(date, sub_unique_items, non_obsolete_items)
                    #print(len(sub_unique_items_all), len(sub_unique_items))
                    # Add weight for items that were already previously received to be received again
                    #wts = np.array([5 if __ in ___ else 1 for __ in sub_unique_items]) #weights twice for received items priorly
                    #p = wts/(wts.sum()) #convert weights into percentages
                    #print(p)
                    #try:
                    #    sub_class_entry = np.random.choice(sub_unique_items, p = p) #corresponding subclasses
                    #except:
                    #    sub_class_entry = np.random.choice(sub_unique_items) #corresponding subclasses
                    # try and except if the entire item and all its subclasses areobsolete, recall the last three items again
                    try:
                        sub_class_entry = np.random.choice(sub_unique_items) #corresponding subclasses
                    except ValueError:
                        sub_unique_items = [item for item in subclass if _ in item][-2:]
                        sub_class_entry = np.random.choice(sub_unique_items)
                    #print(sub_class_entry)
                    sub_class_item_list.append(sub_class_entry) #append a randomized choice of subclasses
                    ___.append(sub_class_entry) #temporary list for weight assignment only
                    
                # create a sub dataframe that includes transaction dates with the correspondign item for reception
                # The following step is repeated twice on date scale then on subclass scale
                sub_df = pd.DataFrame({'transaction_date': [date]*len(sub_class_item_list),
                                       'transaction': ['reception']*len(sub_class_item_list),
                                       'item_type': sub_class_item_list})
                sub_list_df.append(sub_df) # append to initial empty list
            result_df = pd.concat(sub_list_df, axis = 0).sort_values(by = 'transaction_date').reset_index(drop = True) #concat and drop index
            full_data_list.append(result_df) #append to a list
        full_result_df = pd.concat(full_data_list, axis = 0).sort_values(by = 'transaction_date').reset_index(drop = True) #concat and drop index
        
        return(full_result_df)
    ###########################################################################
    
    items_received = generate_sub_classes_entries()
    
    # Add items in stock to be assumed to originally exist before the analysis starts
    original_items_in_stock = [] #items originally avaialble in stock from 1990s
    for pkup in inventory_material: #drilling list only so far
        original_items_in_stock.extend([key for key in items_received.item_type if pkup in key][:1]) #first 2 elements
    # preparing a dataframe to merge
    original_entry = [datetime(2000, 1, 1, 0, 0, 0)] * len(original_items_in_stock) #first date of year
    original_transaction = ['reception'] * len(original_items_in_stock)
    original_items_df = pd.DataFrame({'transaction_date': original_entry,
                                      'transaction': original_transaction,
                                      'item_type': original_items_in_stock})
    full_reception = pd.concat([original_items_df, items_received], axis = 0).reset_index(drop = True).dropna() #drop nans
    


    return(full_reception) #call the local function

reception_df = show_stock_entries_status()

first_entry = []
descriptions = []
for unique_des in reception_df.item_type.unique():
    descriptions.append(unique_des)
    first_entry.append(reception_df[reception_df.item_type == unique_des].transaction_date.reset_index(drop = True)[0])
    
firts_entry_description = list(zip(descriptions, first_entry))
sorted_first_entry_items = sorted(firts_entry_description, key=lambda x: x[1])

last_entry = []
descriptions = []
for unique_des in reception_df.item_type.unique():
    descriptions.append(unique_des)
    last_entry.append(reception_df[reception_df.item_type == unique_des].transaction_date.reset_index(drop = True).iloc[-1])
    
last_entry_description = list(zip(descriptions, last_entry))
sorted_last_entry_items = sorted(last_entry_description, key=lambda x: x[1])

def replace_item_with_generated_item(pickup_list, first_issue):
    '''
        This function is used to convert the combinations of category into multiple items with different descriptions
        INPUT:
            pickup_list: list of items that are originally pickedup before being changed into subclasses
        OUTPUT:
            same list with different descriptions
            '''
    result = []
    sub_result = []
    max_val = [10 if first_issue.year > 2010 else 5][0]

    for elem in pickup_list:
        if isinstance(elem, list): #check if the element is a list
            for ele in elem:
                sub_result.append(random.choice(generate_stock_items([ele], max_val))) #nested function - re call inside the function
            result.append(sub_result)
        else:
            result.append(random.choice(generate_stock_items([elem], max_val))) #select one item only
    return(result)

def conductor_tubular_combinations(conductor_length_count, first_issue):
    '''
        This function is used to identify all possible combinations of conductor different sizes to be issued on RIG site
        It considers the possibilities that conductors are to be sent to RIG on one or two or three times or not at all
        in case of a sidetrack
        INPUT:
            conductor_length_count: it is the number of casing tubular to be called out for a well
            first_issue: the date at which the first issue was picked up
        OUTPUT:
            Three for #1 pickup, #2 pickups, and #3 pickups correspondingly
                                                                                                                        '''

    global reception_df
    # identify possible conductors to pickup
    conductor_tubular_list = ['30" Conductor', '24" Conductor', '20" CSG', '18 5/8" CSG']
    #all_possible_conductor_tubular_list = generate_stock_items(main_conductor_tubular_list)
    # make sure that we will iterate through valid combinations only that have already been received at stock earlier
    #conductor_tubular_list = [combo for combo in all_possible_conductor_tubular_list if combo in reception_df
    #                          [reception_df.transaction_date < first_issue].item.values.tolist()]
    # Generate all combinations of two or three elements of conductor pipes
    two_element_combinations = list(combinations(conductor_tubular_list, 2))
    three_element_combinations = list(combinations(conductor_tubular_list, 3))

    # Filter combinations to preserve original sorting sequence for conductors issuings for two elements
    sorted_two_element_combinations = [list(combo) for combo in two_element_combinations if
                                        conductor_tubular_list.index(combo[0]) < conductor_tubular_list.index(combo[1])]

    # the same filter applies for three elements
    sorted_three_element_combinations = [list(combo) for combo in three_element_combinations if
                                          conductor_tubular_list.index(combo[0]) < conductor_tubular_list.index(combo[1])
                                          < conductor_tubular_list.index(combo[2])]
    
    # filtered possibilities if conductors were to be issued one time only to the RIG site
    # a copy is used to avoid elements replacement in a later step. A nested list is used so that length of list is alwaus 1
    sorted_one_element_combinations = [(random.choice([[], #no pickup for conductors due to a side track well for example
                                random.choice(sorted_two_element_combinations), #picking two elements of conductors only
                                random.choice(sorted_three_element_combinations), #picking three conductor sizes only
                                conductor_tubular_list]).copy())] #picking the entire four conductor sizes

    ########################################################################
    # calling drilling preps on two issues
    for element in sorted_two_element_combinations:
        # find the conductor size that is not picked during a combination and its index in the original list
        missing_items = list(set(conductor_tubular_list) - set(element))
        missing_indices = [conductor_tubular_list.index(mis_itm) for mis_itm in missing_items]
        for i in range(len(element)):
            ele = element[i]
            for missing_item, missing_index in zip(missing_items, missing_indices):
                # find the conductor size that could be issues before or after this missing conductor size
                if conductor_tubular_list.index(ele) in [missing_index - 1, 
                                                         missing_index + 1]:
                    # randomly select if the missing item will be called out for the RIG site or not with other items
                    missing_item_presence = np.random.choice([True, False], p = [0.05, 0.95]) #75% possibility to recall mltiple items
                    # if it should be present
                    if missing_item_presence:
                        # replace the original one item with two items now
                        _ = [element[i]]
                        _.append(missing_item)
                        # in case three items were concated into a list, merge them as one list only not a nested list
                        _ = [item for sublist in _ for item in (sublist if isinstance(sublist, list) else [sublist])]
                        element[i] = _  
                        
    # Modify all possibilites for two and three pickups
    # Calling drilling preps on three issues
    for element in sorted_three_element_combinations:
        # find the conductor size that is not picked during a combination and its index in the original list
        missing_item = list(set(conductor_tubular_list) - set(element))[0]
        missing_index = conductor_tubular_list.index(missing_item)
        # iterate  through each combination element number to be replacable
        for i in range(len(element)):
            ele = element[i] 
            # find the conductor size that could be issues before or after this missing conductor size
            if conductor_tubular_list.index(ele) in [missing_index - 1, missing_index + 1]:
                # randomly select if the missing item will be called out for the RIG site or not with other items
                missing_item_presence = np.random.choice([True, False], p = [0.05, 0.95])
                # if it should be present
                if missing_item_presence:
                    # replace the original one item with two items now
                    element[i] = sorted([element[i], missing_item])
                        
    # randomly choose a combination and convert it to a subclass
    one_element_combinations = replace_item_with_generated_item((sorted_one_element_combinations), first_issue)
    two_element_combinations = replace_item_with_generated_item(random.choice(sorted_two_element_combinations), first_issue)
    three_element_combinations = replace_item_with_generated_item(random.choice(sorted_three_element_combinations), first_issue)
    
    #print(conductor_length_count, one_element_combinations, two_element_combinations, three_element_combinations)
    # mapping pickup to each pickup orders at a well
    pickup_mapping = {1: one_element_combinations, 2: two_element_combinations, 3: three_element_combinations}
    return(pickup_mapping.get(conductor_length_count))

def drilling_tubular_combinations(tubualr_length_count, first_issue):
    '''
        This function is used to output all possible combinations of drilling tubualar when
        INPUT:
            tubualr_length_count: it is the number of casing tubular to be called out for a well
            first_issue: the date at which the first order was issued
        OUTPUT:
            elements sorted for each possibility from two to six pickups per well
                                                                                                        '''


    def get_pickups(casing_list, number_of_combinations):
        '''
            Local function to output pickup elements for each issuing condition per well
            INPUT:
                casing_list: original casing sizes that could be issued to a well
                number_of_combinations: number of combinations per well based on number of issues
            OUTPUT:
                unique list for pickups for any number of issues per well
                                                                                                            '''
        # making combinations of elements
        if number_of_combinations == 5 or number_of_combinations == 6:
            num_of_combinations = 4
        else:
            num_of_combinations = number_of_combinations
            
        element_combinations = sorted(list(combinations(casing_list, num_of_combinations)))
        pickups = [] #empty list of items pickups

        for combo in element_combinations:
            #sorting list elements according to indices of original list
            sorted_combo = sorted(list(combo), key = lambda x: casing_list.index(x))
             # make sure in two items combination that pcikedup items follow the same sequence proposed manually
            if num_of_combinations == 2:
                if sorted_combo[0][0] != sorted_combo[1][0]:
                    _ = replace_item_with_generated_item(sorted_combo, first_issue)
                    pickups.append(_)
                    # picking unique items only of the list
                    unique_pickups = {tuple((sublist)) for sublist in pickups}
                    # converting it back to a list
                    unique_pickups_list = ([list(item) for item in unique_pickups])
                    break

            else:
                #make sure that each element is prior to the subsequent element and that no item is missing in between 2 casing sizes
                #make sure that no element existed more than twice in the list
                if all(casing_list.index(sorted_combo[i + 1]) - casing_list.index(sorted_combo[i]) <= 1
                       for i in range(num_of_combinations-1)) and \
                   all(casing_list.index(sorted_combo[i]) <= casing_list.index(sorted_combo[i + 1])
                       for i in range(num_of_combinations-1)) and \
                   all(count <= 2 for count in {casing_tubular: sum(casing_tubular in element for element in sorted_combo)\
                                                for casing_tubular in casing_list}.values()):
                    
                    if number_of_combinations == 5:
                        sorted_combo = sorted_combo + np.random.choice(casing_list, 1).tolist()
                        sorted_combo = sorted(sorted_combo, key=extract_numeric_value, reverse = True)

                    elif number_of_combinations == 6:
                        sorted_combo = sorted_combo + np.random.choice(casing_list, 2).tolist()
                        sorted_combo = sorted(sorted_combo, key=extract_numeric_value, reverse = True)
                        
                    _ = replace_item_with_generated_item(sorted_combo, first_issue)
                    pickups.append(_)
                    # picking unique items only of the list
                    unique_pickups = {tuple((sublist)) for sublist in pickups}
                    # converting it back to a list
                    unique_pickups_list = ([list(item) for item in unique_pickups])
                    break #stop once condition is satisfied

            
            
        return(unique_pickups_list)
    
    def extract_numeric_value(s):
        # Use regular expression to extract numeric value from the string
        match = re.search(r'\d+', s)
        return int(match.group()) if match else 0
    
    # lists for casing tubular
    casing_tubular_list = ['13 3/8" CSG', '9 5/8" CSG', '7" CSG', '5" CSG']  


    
    # use multiple IFs instead of slow mapping that requires recalling all combinations in every iteration
    if tubualr_length_count == 2:
        #no combination - known possibility
        unique_tubular_list = random.choice([['13 3/8" CSG', '9 5/8" CSG'], ['9 5/8" CSG', '7" CSG'], ['7" CSG', '5" CSG']]) 

        two_pickups = random.choice(get_pickups(unique_tubular_list, 2))
        return(two_pickups)
    elif tubualr_length_count == 3:
        three_pickups = random.choice(get_pickups(casing_tubular_list, 3))
        return(three_pickups)
    elif tubualr_length_count == 4:
        four_pickups = random.choice(get_pickups(casing_tubular_list, 4))
        return(four_pickups)
    elif tubualr_length_count == 5:
        five_pickups = random.choice(get_pickups(casing_tubular_list, 5))
        return(five_pickups)
    elif tubualr_length_count == 6:
        six_pickups = random.choice(get_pickups(casing_tubular_list, 6))
        return(six_pickups)

def tubing_tubular_combinations(tubing_length_count, first_issue):
    '''
        This function is used to identify all possible combinations of tubing different sizes to be issued on RIG site
        It considers the possibilities that tubing tubular are to be sent to RIG on one or two times
        in case of a sidetrack
        INPUT:
            tubing_length_count: it is the number of tubing tubular to be called out for a well
            first_issue: the date at which the first issue was picked up
        OUTPUT:
            Pickups for each count
                                                                                                                        '''
    
    #identify possible tubing sizes to pickup from noting that 4 1/2" tubing shall not be picked up with 5" CSG
    completion_tubular_list = ['2 7/8" Tubing', '3 1/2" Tubing', '4 1/2" Tubing']
    completion_dual_producer = ['2 7/8" Tubing', '3 1/2" Tubing']
    
    one_element_pickup = [np.random.choice(completion_tubular_list)] #picking up one element only
    sorted_one_element_combinations = [one_element_pickup*np.random.randint(1,3)] #this element could conssit of multiple tubing same size different criterai
    two_element_pickup = [np.random.choice(completion_tubular_list)] #two times pickup
    sorted_two_element_combinations = [two_element_pickup*np.random.randint(1,3), two_element_pickup]
    
    one_element_combinations = replace_item_with_generated_item((sorted_one_element_combinations), first_issue)
    # flatten a two eleemnt list
    for each_pickup in sorted_two_element_combinations:
        for i in range(len(each_pickup)):
            each_pickup[i] = replace_item_with_generated_item([each_pickup[i]], first_issue)
    two_element_combinations = []
    for ls in sorted_two_element_combinations:
        two_element_combinations.append([item for sublist in ls for item in sublist])
        
    pickup_mapping = {1: one_element_combinations, 2: two_element_combinations}
    return(pickup_mapping.get(tubing_length_count))

def completion_templates():
    '''
        This function is used to output diverse completion templates that could be run in the well
        OUTPUT:
            different possible completion templates for a specific well
                                                                                                                    '''
    ###################### NATURALLY PRODUCING WELLS ######################
    #single selective well
    template_one = ['WLEG', 'permanent packer', 'retrievable pkr', 'SSD', 'blast joint', 'bottom no-go-nipple',
                    'top no-go nipple', 'perforated pup joint', 'flow coupling'] 
    #possibility for tubing or wirleine retrievable SCSSSV
    template_one.extend(np.random.choice([['WLSCSSSV', 'landing nipple'], ['TRSCSSSV']]))
    # option to add expnasion joing or surge disk based on the design
    template_one.extend(np.random.choice([['expansion joint'], []]))
    template_one.extend(np.random.choice([['surge disk'], []]))

    #single simple well
    template_two = ['WLEG', 'bottom no-go-nipple', 'top no-go nipple',
                    'perforated pup joint', 'flow coupling']
    #possibility for tubing or wirleine retrievable SCSSSV
    template_two.extend(np.random.choice([['WLSCSSSV', 'landing nipple'], ['TRSCSSSV']]))
    # option to add expnasion joing or surge disk based on the design
    template_two.extend(np.random.choice([['surge disk'], []]))
    template_two.extend([np.random.choice(['retrievable pkr', 'permanent packer', 'sealbore packer'])])
    
    
    return(template_one, template_two)    

def completion_equipment_combinations(completion_length_count, first_issue):
    '''
        This function is used to identify all possible combinations of completion different sizes to be issued on RIG site
        It considers the possibilities that completion equipment are to be sent to RIG on one or two times
        in case of a sidetrack
        INPUT:
            completion_length_count: it is the number of completion equipment to be called out for a well
            first_issue: the date at which the first issue was picked up
        OUTPUT:
            Pickups for each count
                                                                                                                        '''
    
    single_pickup = np.random.choice(completion_templates()) #selecting a template to be picked up for a well
    # possibility that some items are issued to the RIG site again
    num_to_select = int(len(single_pickup) / np.random.randint(2,8))
    # addiitonal items to be issued for a second time
    additional_elements = list(np.random.choice(single_pickup, size = num_to_select, replace = False))
    two_pickups = [single_pickup, additional_elements]
    
    one_element_combinations = [replace_item_with_generated_item((single_pickup), first_issue)]
    # flatten a two eleemnt list
    for each_pickup in two_pickups:
        for i in range(len(each_pickup)):
            each_pickup[i] = replace_item_with_generated_item([each_pickup[i]], first_issue)
    two_element_combinations = []
    for ls in two_pickups:
        two_element_combinations.append([item for sublist in ls for item in sublist])    

    pickup_mapping = {1: one_element_combinations, 2: two_element_combinations}
    
    return(pickup_mapping.get(completion_length_count))

def generate_pickups_preserving_entries_dates(pickup_item, length_of_items, first_issue):
    '''
        This function is used to make sure that every issued item on a well, was already received in the stock priorly
        INPUT:
            pickup_item: string of the item category to be issued 
            length_of_items: int of length of items to be issued on same category
            first_issue: the date at which the first order was issued
        OUTPUT:
            item_pickup: list of items issued on the assigned well under the same category
        '''
    


    # A while loop to make sure that no item is issued before it had been received as an entry in the stock
    while True:
        #print('inside loop')
        # try a loop to see if any error raises, then keep retrying till solved

        while True:
            try:
                # if condition rather than the slow mapping 
                if pickup_item == 'drilling prep':
                    item_pickup = conductor_tubular_combinations(length_of_items, first_issue)
                elif pickup_item == 'drilling tubular':
                    item_pickup = drilling_tubular_combinations(length_of_items, first_issue)
                elif pickup_item == 'completion tubular':
                    item_pickup = tubing_tubular_combinations(length_of_items, first_issue)
                elif pickup_item == 'completion equipment':
                    item_pickup = completion_equipment_combinations(length_of_items, first_issue)
                break
            except:
                #print('Retry')
                pass

        # Flattening all items that are picked up for a well, including list of items issued on same day as a list
        flat_list = [item for sublist in item_pickup for item in sublist if type(sublist) == list] #list elements
        original_elements = [item for item in item_pickup if type(item) != list] #string elements
        # combine both elements into a new list
        pickup_list = flat_list + original_elements
        #print(pickup_list)
        reasonable_issue = True
        for _ in pickup_list:
            #making sure that the issue is false if the item was not received at all in the stock
            # or in the case that issuing data was earlier than entry data making no sense
            if _ not in dict(sorted_first_entry_items).keys() or dict(sorted_first_entry_items)[_] > first_issue:
                reasonable_issue = False
                break
        if reasonable_issue:
            #print('End......................................................')
            break  # Exit the while loop if reasonable_issue is True
        else:
            # If reasonable_issue is False, repeat the loop
            #print('not reasnoable issue')
            #print('xxxxxxxxxxxxxxxxxxxxxxx')
            continue 
            
    return(item_pickup)

first_entry = []
descriptions = []
for unique_des in reception_df.item_type.unique():
    descriptions.append(unique_des)
    first_entry.append(reception_df[reception_df.item_type == unique_des].transaction_date.reset_index(drop = True)[0])
    
firts_entry_description = list(zip(descriptions, first_entry))
sorted_first_entry_items = sorted(firts_entry_description, key=lambda x: x[1])


last_entry = []
descriptions = []
for unique_des in reception_df.item_type.unique():
    descriptions.append(unique_des)
    last_entry.append(reception_df[reception_df.item_type == unique_des].transaction_date.reset_index(drop = True).iloc[-1])
    
last_entry_description = list(zip(descriptions, last_entry))
sorted_last_entry_items = sorted(last_entry_description, key=lambda x: x[1])

issue_df = issue_return_df[issue_return_df.transaction == 'issue']
for unique_well in issue_df.well.unique():
    issue_df_well = issue_df[issue_df.well == unique_well]
    well_issues_categories = issue_df_well.transaction_category

transactions = ['drilling prep', 'drilling tubular', 'completion tubular', 'completion equipment'] #transactions of issues
drilling_issue_df = issue_df[issue_df.transaction_category.str.contains('|'.join(transactions))]
drilling_return_df = issue_return_df[issue_return_df.transaction == 'return']


# sorted transactions = ['comletion equipment', 'completion tubular', 'drilling prep', 'drilling tubular', 
#                        'drilling wellhead', 'xmass tree']
pickups = []
for well_name in drilling_issue_df.well.unique(): #iterate through transactions of each well
    print(well_name)
    well_issue_df = drilling_issue_df[drilling_issue_df.well == well_name].sort_values(by = 'transaction_category') #sort data alphabetically
    first_issue_date_well = well_issue_df.transaction_date.min() #first date of issuings assigned to that well
    print(first_issue_date_well)
    transactions_count = [] #initiate list
    for transaction in transactions: #iterate
        trans_len = sum([1 if transaction in item else 0 for item in #count number of item issuings across a well
                     well_issue_df.transaction_category.values.tolist()])

        # Append transaction list of unique items accoringly based on type of transaction
        if transaction == 'drilling prep':
            pickups.extend(generate_pickups_preserving_entries_dates(transaction, trans_len, first_issue_date_well))
        elif transaction == 'drilling tubular':
            pickups.extend(generate_pickups_preserving_entries_dates(transaction, trans_len, first_issue_date_well))
        elif transaction == 'completion tubular':
            pickups.extend(generate_pickups_preserving_entries_dates(transaction, trans_len, first_issue_date_well))
        elif transaction == 'completion equipment':
            pickups.extend(generate_pickups_preserving_entries_dates(transaction, trans_len, first_issue_date_well))
            
        transactions_count.append(trans_len) #list for each well showing corresponding items transactions
drilling_issue_df['item_type'] = pickups #add a column for pickups
# explode each row if a list existed in item_type column, so that the row is duplicated with same data
drilling_issue_df_explode = drilling_issue_df.explode('item_type').reset_index(drop = True)

# merge dataframes to show return items accroding to issued items
drilling_return_df_explode = pd.merge(drilling_return_df, drilling_issue_df_explode[['well', 'transaction_category', 'item_type']], 
                     on = ['well', 'transaction_category'], how='left')

drilling_df_result = pd.concat([drilling_issue_df_explode, drilling_return_df_explode])\
                    .sort_values(by = ['well', 'transaction_date']).dropna().drop_duplicates().reset_index(drop = True)


#######################################################################
unique_drilling_items = drilling_df_result.item_type.unique() #unique items in stock
tran_df = pd.concat([drilling_df_result.drop(['well', 'transaction_category'], axis = 1), reception_df]).sort_values(by = ['item_type', 'transaction_date']).reset_index(drop = True)
tran_df = tran_df[tran_df.item_type.apply(lambda x: x in unique_drilling_items)]
sorted_drilling_df = tran_df[tran_df.item_type.apply(lambda x: x in unique_drilling_items)].drop_duplicates()
sorted_drilling_df['transaction_date'] = sorted_drilling_df['transaction_date'].dt.strftime('%Y-%m-%d') #output type


# count category occurrence for the final ouptut table
count_items = pd.DataFrame(sorted_drilling_df[sorted_drilling_df['transaction'] == 'issue'].item_type.value_counts()).reset_index()
count_items['item_group'] = count_items['index'].str.extract(r'(\d+ ?\d*/?\d*"? CSG|Conductor)')
grouped_data = count_items.groupby('item_group')['item_type'].sum().reset_index()

condition_met = False

# Check conditions
condition1_met = (grouped_data.loc[grouped_data['item_group'] == '9 5/8" CSG', 'item_type'].values[0] 
               <= grouped_data.loc[grouped_data['item_group'] == '13 3/8" CSG', 'item_type'].values[0] * 1.10 
               and grouped_data.loc[grouped_data['item_group'] == '9 5/8" CSG', 'item_type'].values[0] 
               >= grouped_data.loc[grouped_data['item_group'] == '13 3/8" CSG', 'item_type'].values[0] * 0.90)
condition2_met = (grouped_data.loc[grouped_data['item_group'] == '7" CSG', 'item_type'].values[0] 
               < grouped_data.loc[grouped_data['item_group'] == '9 5/8" CSG', 'item_type'].values[0])
condition3_met = (grouped_data.loc[grouped_data['item_group'] == '5" CSG', 'item_type'].values[0] 
               < grouped_data.loc[grouped_data['item_group'] == '7" CSG', 'item_type'].values[0])

condition_met = (condition1_met and condition2_met and condition3_met) #final status of all conditions combined


iteration = 0
while True:
    iteration +=1
    transactions = ['drilling prep', 'drilling tubular'] #transactions of issues
    drilling_issue_df = issue_df[issue_df.transaction_category.str.contains('|'.join(transactions))]
    drilling_return_df = issue_return_df[issue_return_df.transaction == 'return']


    # sorted transactions = ['comletion equipment', 'completion tubular', 'drilling prep', 'drilling tubular', 
    #                        'drilling wellhead', 'xmass tree']
    pickups = []
    for well_name in drilling_issue_df.well.unique(): #iterate through transactions of each well
        print(well_name)
        well_issue_df = drilling_issue_df[drilling_issue_df.well == well_name].sort_values(by = 'transaction_category') #sort data alphabetically
        first_issue_date_well = well_issue_df.transaction_date.min() #last date of issuings assigned to that well
        print(first_issue_date_well)
        transactions_count = [] #initiate list
        for transaction in transactions: #iterate
            trans_len = sum([1 if transaction in item else 0 for item in #count number of item issuings across a well
                         well_issue_df.transaction_category.values.tolist()])

            # Append transaction list of unique items accoringly based on type of transaction
            if transaction == 'drilling prep':
                pickups.extend(generate_pickups_preserving_entries_dates(transaction, trans_len, first_issue_date_well))
            elif transaction == 'drilling tubular':
                pickups.extend(generate_pickups_preserving_entries_dates(transaction, trans_len, first_issue_date_well))

            transactions_count.append(trans_len) #list for each well showing corresponding items transactions
    drilling_issue_df['item_type'] = pickups #add a column for pickups
    # explode each row if a list existed in item_type column, so that the row is duplicated with same data

    drilling_issue_df_explode = drilling_issue_df.explode('item_type').reset_index(drop = True)

    # merge dataframes to show return items accroding to issued items
    drilling_return_df_explode = pd.merge(drilling_return_df, drilling_issue_df_explode[['well', 'transaction_category', 'item_type']], 
                         on = ['well', 'transaction_category'], how='left')

    drilling_df_result = pd.concat([drilling_issue_df_explode, drilling_return_df_explode])\
                        .sort_values(by = ['well', 'transaction_date']).dropna().drop_duplicates().reset_index(drop = True)


    #######################################################################
    unique_drilling_items = drilling_df_result.item_type.unique() #unique items in stock
    tran_df = pd.concat([drilling_df_result.drop(['well', 'transaction_category'], axis = 1), reception_df]).sort_values(by = ['item_type', 'transaction_date']).reset_index(drop = True)
    tran_df = tran_df[tran_df.item_type.apply(lambda x: x in unique_drilling_items)]
    sorted_drilling_df = tran_df[tran_df.item_type.apply(lambda x: x in unique_drilling_items)].drop_duplicates()
    sorted_drilling_df['transaction_date'] = sorted_drilling_df['transaction_date'].dt.strftime('%Y-%m-%d') #output type


    # count category occurrence for the final ouptut table
    count_items = pd.DataFrame(sorted_drilling_df[sorted_drilling_df['transaction'] == 'issue'].item_type.value_counts()).reset_index()
    count_items['item_group'] = count_items['index'].str.extract(r'(\d+ ?\d*/?\d*"? CSG|Conductor)')
    grouped_data = count_items.groupby('item_group')['item_type'].sum().reset_index()
    
    condition_met = False
    
    # Check conditions
    condition1_met = (grouped_data.loc[grouped_data['item_group'] == '9 5/8" CSG', 'item_type'].values[0] 
                   <= grouped_data.loc[grouped_data['item_group'] == '13 3/8" CSG', 'item_type'].values[0] * 1.10 
                   and grouped_data.loc[grouped_data['item_group'] == '9 5/8" CSG', 'item_type'].values[0] 
                   >= grouped_data.loc[grouped_data['item_group'] == '13 3/8" CSG', 'item_type'].values[0] * 0.90)
    condition2_met = (grouped_data.loc[grouped_data['item_group'] == '7" CSG', 'item_type'].values[0] 
                   < grouped_data.loc[grouped_data['item_group'] == '9 5/8" CSG', 'item_type'].values[0])
    condition3_met = (grouped_data.loc[grouped_data['item_group'] == '5" CSG', 'item_type'].values[0] 
                   < grouped_data.loc[grouped_data['item_group'] == '7" CSG', 'item_type'].values[0])
    
    condition_met = (condition1_met and condition2_met and condition3_met) #final status of all conditions combined
    
    # if all conditions are satisified
    if condition_met:
        break
    else:
        print('Re-iteration number: ', iteration)


drilling_SKUs_list= []

# END_date: date after which no issues should be issued for an item - a 2-5 years period after last entry date
# last_possible_reception_date: 
for item in sorted_drilling_df.item_type.unique():
    print(item)
    random_duration = np.random.randint(2,5)
    df_itemized = sorted_drilling_df[sorted_drilling_df.item_type == item]
    df_itemized['transaction_date'] = pd.to_datetime(df_itemized['transaction_date'])
    
    first_issue_date = df_itemized['transaction_date'].min()
    last_issue_date = df_itemized['transaction_date'].max()
    # Mark the end of transacgtions for an item with END transaction type
    first_entry_date = dict(sorted_first_entry_items)[item]
    last_entry_date = dict(sorted_last_entry_items)[item]
    df_itemized = df_itemized.append({'transaction_date': last_entry_date + timedelta(days = 365*random_duration),
                                      'transaction': 'END', 'item_type': item}, ignore_index = True).sort_values(by = 'transaction_date').reset_index(drop = True)      
    # Identify end date of transactions and last date of actual issue that should be transformed later to another category
    END_date = df_itemized[df_itemized['transaction'] == 'END']['transaction_date'].values
    END_date = pd.to_datetime(pd.to_datetime(END_date).strftime('%Y-%m-%d %H:%M:%S')[0])

    #################################################################################
    
    # items that those transactions could be move to if it was issued after last possible date
    last_possible_reception_date = max(END_date, last_issue_date - timedelta(days = 365*4))
    replaceable_items = [cat for cat in sorted_drilling_df.item_type.unique()
                        if (item.split('-')[0] in cat) and (item != cat)
                        and (dict(sorted_last_entry_items)[cat] > last_possible_reception_date)
                        and (dict(sorted_first_entry_items)[cat] < END_date)]
    #print(replaceable_items)
    
    # if there is an item that validates the criterai
    if replaceable_items:
        # select one item from the list
        picked_item = np.random.choice(replaceable_items)
        # all transactions after END date would be moved to this new item
        df_itemized.loc[df_itemized[df_itemized['transaction'] == 'END'].index[0] + 1:, 'item_type'] = picked_item
        
    # in case there is no single item could cover the entire period, divide duration between end date and last issue into chunks
    else:
        # If replaceable_items is empty, divide final_date into chunks
        chunk_size = ((last_issue_date - END_date) // 5).days  # Choose an appropriate chunk size
        chunks = np.arange(END_date, last_issue_date, timedelta(days=chunk_size))
        for start_date, end_date in zip(chunks[:-1], chunks[1:]): #start and end date for a chunk
            start_date, end_date = pd.to_datetime(start_date), pd.to_datetime(end_date) #convert formats
            last_possible_reception_date_chunk = max(end_date - timedelta(days = 365*4), start_date)
            replaceable_items_chunk = [cat for cat in sorted_drilling_df.item_type.unique()
                                        if (item.split('-')[0] in cat) and (item != cat)
                                        and (dict(sorted_last_entry_items)[cat] > last_possible_reception_date_chunk)
                                        and (dict(sorted_first_entry_items)[cat] < start_date)]
            # Process replaceable_items_chunk or perform other actions
            if replaceable_items_chunk != []:
                picked_item = np.random.choice(replaceable_items_chunk)
                df_itemized.loc[df_itemized[(df_itemized['transaction_date'] >= start_date) &
                                            (df_itemized['transaction_date'] <= end_date)].index, 'item_type'] = picked_item
                print('PASS')
            else:
                if END_date.year < 2023:
                    print('###############################DEFINITE FAILURE###############################')
                    df_itemized = df_itemized.drop(df_itemized[(df_itemized['transaction_date'] >= start_date) &
                                                               (df_itemized['transaction_date'] <= end_date)].index)
                    #df_itemized.loc[df_itemized[(df_itemized['transaction_date'] >= start_date) &
                    #                            (df_itemized['transaction_date'] <= end_date)].index, 'transaction'] = 'DROP'
   
    ####################################################################################          
    
    # Sign the beginning and End of reception/issue for each item
    df_itemized = df_itemized[~df_itemized['transaction'].str.contains('END')]
    # Identify end date of transactions and last date of actual issue that should be transformed later to another category
    df_itemized = df_itemized.append({'transaction_date': END_date,
                                      'transaction': 'END', 'item_type': item}, ignore_index = True).sort_values(by = ['transaction_date', 'transaction']).reset_index(drop = True)      
    #df_itemized = df_itemized.append({'transaction_date': first_entry_date,
    #                                  'transaction': 'BEGIN', 'item_type': item}, ignore_index = True).sort_values(by = ['transaction_date', 'transaction']).reset_index(drop = True)     
    # drop End date row and any transaction that occurred after it
    # Drop rows from the index of end date onward
    df_itemized = df_itemized.iloc[:df_itemized[df_itemized['transaction'] == 'END'].index[0]]

    ####################################################################################        
    
    drilling_SKUs_list.append(df_itemized)
    
drilling_SKUs_df_prep = pd.concat(drilling_SKUs_list, axis = 0).sort_values(by = ['item_type', 'transaction_date']).reset_index(drop = True)
unique_drilling_SKUs_prep = drilling_SKUs_df_prep.item_type.unique() #unique items in stock


with PdfPages('output_tables.pdf') as pdf:
    for item_type in unique_drilling_SKUs:
        print(item_type)
        # Select the data for the current 'item_type'
        table_data = drilling_SKUs_df[drilling_SKUs_df['item_type'] == item_type].copy()

        # Create a table using Matplotlib
        fig, ax = plt.subplots(figsize=(20, 8))
        ax.axis('off')  # Turn off axis labels

        # Apply styling to change font color to green for 'reception' rows
        cell_colors = [['lightgreen' if val == 'reception' else 'lightyellow' if val == 'return'
                        else 'lightcoral' if val == 'issue' else 'black' if val == 'BEGIN' 
                        else 'black' if val == 'END' else 'purple' if val == 'DROP' 
                        else 'white' for val in row] for row in table_data.values]

        table = ax.table(cellText=table_data.values,
                         colLabels=table_data.columns,
                         cellLoc='center',
                         loc='center',
                         cellColours=cell_colors)

        table.auto_set_font_size(False)  # Set font size
        table.set_fontsize(8)  # Font size

        # Set font color for the entire table
        for i in range(len(cell_colors)):
            for j in range(len(cell_colors[i])):
                cell = table[i+1, j]  # +1 to account for header row
                cell.set_text_props(color='black')  # Set text color to black

        # Add the plot to the PDF file
        pdf.savefig(fig, bbox_inches='tight')  # Ensure the entire table length is captured
        plt.close()