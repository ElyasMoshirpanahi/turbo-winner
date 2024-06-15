from scripts.hamster import HamsterCombat
h = HamsterCombat( url="https://app.hamsterkombat.io/clicker/?tgWebAppStartParam=kentId6135970338#tgWebAppData=user%3D%257B%2522id%2522%253A7411057643%252C%2522first_name%2522%253A%2522Polic%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522username%2522%253A%2522Boalss%2522%252C%2522language_code%2522%253A%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%257D%26chat_instance%3D8691240196128113547%26chat_type%3Dprivate%26start_param%3DkentId6135970338%26auth_date%3D1718194661%26hash%3Dcebd0a2900b55a99a18c9e34a1f1bd4fdc5eece193d636fb79933554cf722109&tgWebAppVersion=7.4&tgWebAppPlatform=ios",
                  max_days_for_return=20,
                  client_id=7411057643,auto_upgrade=False)

# timex = time.time() *1000
upgrade_id = "Licence North America"
h.upgrade_item(upgrade_name=upgrade_id)