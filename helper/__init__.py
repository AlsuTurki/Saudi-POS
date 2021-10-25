
# clean city and sector columns ar & eng
def cities(df):
    df['English_City'] = df["City"].copy()
    df['English_City'][df.English_City.str.contains('TABOUK')] = 'TABOUK'
    df['English_City'][df.English_City.str.contains('HAIL')] = 'HAIL'
    df['English_City'][df.English_City.str.contains('ABHA')] = 'ABHA'
    df['English_City'][df.English_City.str.contains('MAKKAH')] = 'MAKKAH'
    df['English_City'][df.English_City.str.contains('BURAIDAH')] = 'BURAIDAH'
    df['English_City'][df.English_City.str.contains('KHOBAR')] = 'KHOBAR'
    df['English_City'][df.English_City.str.contains('MADINA')] = 'MADINA'
    df['English_City'][df.English_City.str.contains('DAMMAM')] = 'DAMMAM'
    df['English_City'][df.English_City.str.contains('JEDDAH')] = 'JEDDAH'
    df['English_City'][df.English_City.str.contains('RIYADH')] = 'RIYADH'
    df['English_City'][df.English_City.str.contains('OTHER')] = 'OTHER'

    df['Arabic_City'] = df["City"].copy()
    df['Arabic_City'][df.Arabic_City.str.contains('TABOUK')] = 'تبوك'
    df['Arabic_City'][df.Arabic_City.str.contains('HAIL')] = 'حائل'
    df['Arabic_City'][df.Arabic_City.str.contains('ABHA')] = 'أبها'
    df['Arabic_City'][df.Arabic_City.str.contains('MAKKAH')] = 'مكة المكرمة'
    df['Arabic_City'][df.Arabic_City.str.contains('BURAIDAH')] = 'بريدة'
    df['Arabic_City'][df.Arabic_City.str.contains('KHOBAR')] = 'الخبر'
    df['Arabic_City'][df.Arabic_City.str.contains('MADINA')] = 'المنورة'
    df['Arabic_City'][df.Arabic_City.str.contains('DAMMAM')] = 'الدمام'
    df['Arabic_City'][df.Arabic_City.str.contains('JEDDAH')] = 'جدة'
    df['Arabic_City'][df.Arabic_City.str.contains('RIYADH')] = 'الرياض'
    df['Arabic_City'][df.Arabic_City.str.contains('OTHER')] = 'المدن الأخرى'

    del df["City"]

def sectors(df):
    df['English_Sector'] = df["Sector"].copy()
    df['English_Sector'][df.English_Sector.str.contains('Clothing')] = 'Clothing and Footwear'
    df['English_Sector'][df.English_Sector.str.contains('Construction')] = 'Construction & Building Materials'
    df['English_Sector'][df.English_Sector.str.contains('Education')] = 'Education'
    df['English_Sector'][df.English_Sector.str.contains('Electronic')] = 'Electronic & Electric Devices'
    df['English_Sector'][df.English_Sector.str.contains('Gas')] = 'Gas'
    df['English_Sector'][df.English_Sector.str.contains('Health')] = 'Health'
    df['English_Sector'][df.English_Sector.str.contains('Furniture')] = 'Furniture'
    df['English_Sector'][df.English_Sector.str.contains('Hotels')] = 'Hotels'
    df['English_Sector'][df.English_Sector.str.contains('Public')] = 'Public Utilities'
    df['English_Sector'][df.English_Sector.str.contains('Jewelry')] = 'Jewelry'
    df['English_Sector'][df.English_Sector.str.contains('Miscellaneous')] = 'Miscellaneous Goods and Services'
    df['English_Sector'][df.English_Sector.str.contains('Recreation')] = 'Recreation and Culture'
    df['English_Sector'][df.English_Sector.str.contains('Culture')] = 'Recreation and Culture'
    df['English_Sector'][df.English_Sector.str.contains('Restaurants')] = 'Restaurants & Café'
    df['English_Sector'][df.English_Sector.str.contains('Beverage')] = 'Beverage and Food'
    df['English_Sector'][df.English_Sector.str.contains('Telecommunication')] = 'Telecommunication'
    df['English_Sector'][df.English_Sector.str.contains('Transportation')] = 'Transportation'
    df['English_Sector'][df.English_Sector.str.contains('Other')] = 'Other'
    df['English_Sector'][df.English_Sector.str.contains('Total')] = 'Total'

    df['Arabic_Sector'] = df["Sector"].copy()
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Clothing')] = 'الملابس والأحذية'
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Construction')] = 'مواد التشييد والبناء'
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Education')] = 'التعليم'
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Electronic')] = 'الأجهزة الإلكترونية والكهربائية'
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Gas')] = 'محطات الوقود'
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Health')] = 'الصحة'
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Furniture')] = 'الأثاث'
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Hotels')] = 'الفنادق'
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Public')] = 'المنافع العامة'
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Jewelry')] = 'المجوهرات'
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Miscellaneous')] = 'سلع وخدمات متنوعة'
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Recreation')] = 'الترفية والثقافة'
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Culture')] = 'الترفية والثقافة'
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Restaurants')] = 'المطاعم والمقاهي'
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Beverage')] = 'الأطعمة والمشروبات'
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Telecommunication')] = 'الاتصالات'
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Transportation')] = 'المواصلات'
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Other')] = 'أخرى'
    df['Arabic_Sector'][df.Arabic_Sector.str.contains('Total')] = 'الإجمالي'

    del df["Sector"]


# to intger
def to_int(df,x):
    df[x] = df[x].replace(',','', regex=True)
    df[x] = df[x].astype(int)