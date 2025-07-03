import re

def parse_user_query(query):
    # regex-based extraction 
    ram = re.search(r'(\d+)\s*GB\s*RAM', query, re.I)
    cpu = re.search(r'(Intel|AMD)[^, ]*', query, re.I)
    ssd = re.search(r'(\d+)\s*GB\s*SSD', query, re.I)
    hdd = re.search(r'(\d+)\s*GB\s*HDD', query, re.I)
    gpu = re.search(r'(NVIDIA|AMD|Intel)[^, ]*', query, re.I)
    os = re.search(r'(Windows|Mac|Linux|Ubuntu)', query, re.I)
    price = re.search(r'under\s*₹?(\d+)', query, re.I)
    brand = re.search(r'(Apple|Dell|HP|Lenovo|Acer|Asus|MSI|Microsoft|Razer|Samsung|Toshiba|Fujitsu|Google)', query, re.I)


    return {
        'Company': brand.group(1) if brand else "N/A",
        'TypeName': "N/A",  #can be elaborated
        'Ram': ram.group(1) if ram else "N/A",
        'Cpu_brand': cpu.group(1) if cpu else "N/A",
        'SSD': ssd.group(1) if ssd else "0",
        'HDD': hdd.group(1) if hdd else "0",
        'Gpu_brand': gpu.group(1) if gpu else "N/A",
        'Os': os.group(1) if os else "N/A",
        'Price': price.group(1) if price else "N/A"
    }