# Generated by Django 3.1.10 on 2024-11-21 15:53

from django.db import migrations

import vendor.timezones.fields


class Migration(migrations.Migration):
    dependencies = [
        ("profile", "0014_auto_20240709_1228"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="timezone",
            field=vendor.timezones.fields.TimeZoneField(
                choices=[
                    ("Africa/Abidjan", "(GMT+0000) Africa/Abidjan"),
                    ("Africa/Accra", "(GMT+0000) Africa/Accra"),
                    ("Africa/Addis_Ababa", "(GMT+0300) Africa/Addis_Ababa"),
                    ("Africa/Algiers", "(GMT+0100) Africa/Algiers"),
                    ("Africa/Asmara", "(GMT+0300) Africa/Asmara"),
                    ("Africa/Bamako", "(GMT+0000) Africa/Bamako"),
                    ("Africa/Bangui", "(GMT+0100) Africa/Bangui"),
                    ("Africa/Banjul", "(GMT+0000) Africa/Banjul"),
                    ("Africa/Bissau", "(GMT+0000) Africa/Bissau"),
                    ("Africa/Blantyre", "(GMT+0200) Africa/Blantyre"),
                    ("Africa/Brazzaville", "(GMT+0100) Africa/Brazzaville"),
                    ("Africa/Bujumbura", "(GMT+0200) Africa/Bujumbura"),
                    ("Africa/Cairo", "(GMT+0200) Africa/Cairo"),
                    ("Africa/Casablanca", "(GMT+0100) Africa/Casablanca"),
                    ("Africa/Ceuta", "(GMT+0100) Africa/Ceuta"),
                    ("Africa/Conakry", "(GMT+0000) Africa/Conakry"),
                    ("Africa/Dakar", "(GMT+0000) Africa/Dakar"),
                    ("Africa/Dar_es_Salaam", "(GMT+0300) Africa/Dar_es_Salaam"),
                    ("Africa/Djibouti", "(GMT+0300) Africa/Djibouti"),
                    ("Africa/Douala", "(GMT+0100) Africa/Douala"),
                    ("Africa/El_Aaiun", "(GMT+0100) Africa/El_Aaiun"),
                    ("Africa/Freetown", "(GMT+0000) Africa/Freetown"),
                    ("Africa/Gaborone", "(GMT+0200) Africa/Gaborone"),
                    ("Africa/Harare", "(GMT+0200) Africa/Harare"),
                    ("Africa/Johannesburg", "(GMT+0200) Africa/Johannesburg"),
                    ("Africa/Juba", "(GMT+0300) Africa/Juba"),
                    ("Africa/Kampala", "(GMT+0300) Africa/Kampala"),
                    ("Africa/Khartoum", "(GMT+0200) Africa/Khartoum"),
                    ("Africa/Kigali", "(GMT+0200) Africa/Kigali"),
                    ("Africa/Kinshasa", "(GMT+0100) Africa/Kinshasa"),
                    ("Africa/Lagos", "(GMT+0100) Africa/Lagos"),
                    ("Africa/Libreville", "(GMT+0100) Africa/Libreville"),
                    ("Africa/Lome", "(GMT+0000) Africa/Lome"),
                    ("Africa/Luanda", "(GMT+0100) Africa/Luanda"),
                    ("Africa/Lubumbashi", "(GMT+0200) Africa/Lubumbashi"),
                    ("Africa/Lusaka", "(GMT+0200) Africa/Lusaka"),
                    ("Africa/Malabo", "(GMT+0100) Africa/Malabo"),
                    ("Africa/Maputo", "(GMT+0200) Africa/Maputo"),
                    ("Africa/Maseru", "(GMT+0200) Africa/Maseru"),
                    ("Africa/Mbabane", "(GMT+0200) Africa/Mbabane"),
                    ("Africa/Mogadishu", "(GMT+0300) Africa/Mogadishu"),
                    ("Africa/Monrovia", "(GMT+0000) Africa/Monrovia"),
                    ("Africa/Nairobi", "(GMT+0300) Africa/Nairobi"),
                    ("Africa/Ndjamena", "(GMT+0100) Africa/Ndjamena"),
                    ("Africa/Niamey", "(GMT+0100) Africa/Niamey"),
                    ("Africa/Nouakchott", "(GMT+0000) Africa/Nouakchott"),
                    ("Africa/Ouagadougou", "(GMT+0000) Africa/Ouagadougou"),
                    ("Africa/Porto-Novo", "(GMT+0100) Africa/Porto-Novo"),
                    ("Africa/Sao_Tome", "(GMT+0000) Africa/Sao_Tome"),
                    ("Africa/Tripoli", "(GMT+0200) Africa/Tripoli"),
                    ("Africa/Tunis", "(GMT+0100) Africa/Tunis"),
                    ("Africa/Windhoek", "(GMT+0200) Africa/Windhoek"),
                    ("America/Adak", "(GMT-1000) America/Adak"),
                    ("America/Anchorage", "(GMT-0900) America/Anchorage"),
                    ("America/Anguilla", "(GMT-0400) America/Anguilla"),
                    ("America/Antigua", "(GMT-0400) America/Antigua"),
                    ("America/Araguaina", "(GMT-0300) America/Araguaina"),
                    ("America/Argentina/Buenos_Aires", "(GMT-0300) America/Argentina/Buenos_Aires"),
                    ("America/Argentina/Catamarca", "(GMT-0300) America/Argentina/Catamarca"),
                    ("America/Argentina/Cordoba", "(GMT-0300) America/Argentina/Cordoba"),
                    ("America/Argentina/Jujuy", "(GMT-0300) America/Argentina/Jujuy"),
                    ("America/Argentina/La_Rioja", "(GMT-0300) America/Argentina/La_Rioja"),
                    ("America/Argentina/Mendoza", "(GMT-0300) America/Argentina/Mendoza"),
                    ("America/Argentina/Rio_Gallegos", "(GMT-0300) America/Argentina/Rio_Gallegos"),
                    ("America/Argentina/Salta", "(GMT-0300) America/Argentina/Salta"),
                    ("America/Argentina/San_Juan", "(GMT-0300) America/Argentina/San_Juan"),
                    ("America/Argentina/San_Luis", "(GMT-0300) America/Argentina/San_Luis"),
                    ("America/Argentina/Tucuman", "(GMT-0300) America/Argentina/Tucuman"),
                    ("America/Argentina/Ushuaia", "(GMT-0300) America/Argentina/Ushuaia"),
                    ("America/Aruba", "(GMT-0400) America/Aruba"),
                    ("America/Asuncion", "(GMT-0300) America/Asuncion"),
                    ("America/Atikokan", "(GMT-0500) America/Atikokan"),
                    ("America/Bahia", "(GMT-0300) America/Bahia"),
                    ("America/Bahia_Banderas", "(GMT-0600) America/Bahia_Banderas"),
                    ("America/Barbados", "(GMT-0400) America/Barbados"),
                    ("America/Belem", "(GMT-0300) America/Belem"),
                    ("America/Belize", "(GMT-0600) America/Belize"),
                    ("America/Blanc-Sablon", "(GMT-0400) America/Blanc-Sablon"),
                    ("America/Boa_Vista", "(GMT-0400) America/Boa_Vista"),
                    ("America/Bogota", "(GMT-0500) America/Bogota"),
                    ("America/Boise", "(GMT-0700) America/Boise"),
                    ("America/Cambridge_Bay", "(GMT-0700) America/Cambridge_Bay"),
                    ("America/Campo_Grande", "(GMT-0400) America/Campo_Grande"),
                    ("America/Cancun", "(GMT-0500) America/Cancun"),
                    ("America/Caracas", "(GMT-0400) America/Caracas"),
                    ("America/Cayenne", "(GMT-0300) America/Cayenne"),
                    ("America/Cayman", "(GMT-0500) America/Cayman"),
                    ("America/Chicago", "(GMT-0600) America/Chicago"),
                    ("America/Chihuahua", "(GMT-0700) America/Chihuahua"),
                    ("America/Costa_Rica", "(GMT-0600) America/Costa_Rica"),
                    ("America/Creston", "(GMT-0700) America/Creston"),
                    ("America/Cuiaba", "(GMT-0400) America/Cuiaba"),
                    ("America/Curacao", "(GMT-0400) America/Curacao"),
                    ("America/Danmarkshavn", "(GMT+0000) America/Danmarkshavn"),
                    ("America/Dawson", "(GMT-0700) America/Dawson"),
                    ("America/Dawson_Creek", "(GMT-0700) America/Dawson_Creek"),
                    ("America/Denver", "(GMT-0700) America/Denver"),
                    ("America/Detroit", "(GMT-0500) America/Detroit"),
                    ("America/Dominica", "(GMT-0400) America/Dominica"),
                    ("America/Edmonton", "(GMT-0700) America/Edmonton"),
                    ("America/Eirunepe", "(GMT-0500) America/Eirunepe"),
                    ("America/El_Salvador", "(GMT-0600) America/El_Salvador"),
                    ("America/Fort_Nelson", "(GMT-0700) America/Fort_Nelson"),
                    ("America/Fortaleza", "(GMT-0300) America/Fortaleza"),
                    ("America/Glace_Bay", "(GMT-0400) America/Glace_Bay"),
                    ("America/Goose_Bay", "(GMT-0400) America/Goose_Bay"),
                    ("America/Grand_Turk", "(GMT-0500) America/Grand_Turk"),
                    ("America/Grenada", "(GMT-0400) America/Grenada"),
                    ("America/Guadeloupe", "(GMT-0400) America/Guadeloupe"),
                    ("America/Guatemala", "(GMT-0600) America/Guatemala"),
                    ("America/Guayaquil", "(GMT-0500) America/Guayaquil"),
                    ("America/Guyana", "(GMT-0400) America/Guyana"),
                    ("America/Halifax", "(GMT-0400) America/Halifax"),
                    ("America/Havana", "(GMT-0500) America/Havana"),
                    ("America/Hermosillo", "(GMT-0700) America/Hermosillo"),
                    ("America/Indiana/Indianapolis", "(GMT-0500) America/Indiana/Indianapolis"),
                    ("America/Indiana/Knox", "(GMT-0600) America/Indiana/Knox"),
                    ("America/Indiana/Marengo", "(GMT-0500) America/Indiana/Marengo"),
                    ("America/Indiana/Petersburg", "(GMT-0500) America/Indiana/Petersburg"),
                    ("America/Indiana/Tell_City", "(GMT-0600) America/Indiana/Tell_City"),
                    ("America/Indiana/Vevay", "(GMT-0500) America/Indiana/Vevay"),
                    ("America/Indiana/Vincennes", "(GMT-0500) America/Indiana/Vincennes"),
                    ("America/Indiana/Winamac", "(GMT-0500) America/Indiana/Winamac"),
                    ("America/Inuvik", "(GMT-0700) America/Inuvik"),
                    ("America/Iqaluit", "(GMT-0500) America/Iqaluit"),
                    ("America/Jamaica", "(GMT-0500) America/Jamaica"),
                    ("America/Juneau", "(GMT-0900) America/Juneau"),
                    ("America/Kentucky/Louisville", "(GMT-0500) America/Kentucky/Louisville"),
                    ("America/Kentucky/Monticello", "(GMT-0500) America/Kentucky/Monticello"),
                    ("America/Kralendijk", "(GMT-0400) America/Kralendijk"),
                    ("America/La_Paz", "(GMT-0400) America/La_Paz"),
                    ("America/Lima", "(GMT-0500) America/Lima"),
                    ("America/Los_Angeles", "(GMT-0800) America/Los_Angeles"),
                    ("America/Lower_Princes", "(GMT-0400) America/Lower_Princes"),
                    ("America/Maceio", "(GMT-0300) America/Maceio"),
                    ("America/Managua", "(GMT-0600) America/Managua"),
                    ("America/Manaus", "(GMT-0400) America/Manaus"),
                    ("America/Marigot", "(GMT-0400) America/Marigot"),
                    ("America/Martinique", "(GMT-0400) America/Martinique"),
                    ("America/Matamoros", "(GMT-0600) America/Matamoros"),
                    ("America/Mazatlan", "(GMT-0700) America/Mazatlan"),
                    ("America/Menominee", "(GMT-0600) America/Menominee"),
                    ("America/Merida", "(GMT-0600) America/Merida"),
                    ("America/Metlakatla", "(GMT-0900) America/Metlakatla"),
                    ("America/Mexico_City", "(GMT-0600) America/Mexico_City"),
                    ("America/Miquelon", "(GMT-0300) America/Miquelon"),
                    ("America/Moncton", "(GMT-0400) America/Moncton"),
                    ("America/Monterrey", "(GMT-0600) America/Monterrey"),
                    ("America/Montevideo", "(GMT-0300) America/Montevideo"),
                    ("America/Montserrat", "(GMT-0400) America/Montserrat"),
                    ("America/Nassau", "(GMT-0500) America/Nassau"),
                    ("America/New_York", "(GMT-0500) America/New_York"),
                    ("America/Nipigon", "(GMT-0500) America/Nipigon"),
                    ("America/Nome", "(GMT-0900) America/Nome"),
                    ("America/Noronha", "(GMT-0200) America/Noronha"),
                    ("America/North_Dakota/Beulah", "(GMT-0600) America/North_Dakota/Beulah"),
                    ("America/North_Dakota/Center", "(GMT-0600) America/North_Dakota/Center"),
                    ("America/North_Dakota/New_Salem", "(GMT-0600) America/North_Dakota/New_Salem"),
                    ("America/Nuuk", "(GMT-0300) America/Nuuk"),
                    ("America/Ojinaga", "(GMT-0700) America/Ojinaga"),
                    ("America/Panama", "(GMT-0500) America/Panama"),
                    ("America/Pangnirtung", "(GMT-0500) America/Pangnirtung"),
                    ("America/Paramaribo", "(GMT-0300) America/Paramaribo"),
                    ("America/Phoenix", "(GMT-0700) America/Phoenix"),
                    ("America/Port-au-Prince", "(GMT-0500) America/Port-au-Prince"),
                    ("America/Port_of_Spain", "(GMT-0400) America/Port_of_Spain"),
                    ("America/Porto_Velho", "(GMT-0400) America/Porto_Velho"),
                    ("America/Puerto_Rico", "(GMT-0400) America/Puerto_Rico"),
                    ("America/Punta_Arenas", "(GMT-0300) America/Punta_Arenas"),
                    ("America/Rainy_River", "(GMT-0600) America/Rainy_River"),
                    ("America/Rankin_Inlet", "(GMT-0600) America/Rankin_Inlet"),
                    ("America/Recife", "(GMT-0300) America/Recife"),
                    ("America/Regina", "(GMT-0600) America/Regina"),
                    ("America/Resolute", "(GMT-0600) America/Resolute"),
                    ("America/Rio_Branco", "(GMT-0500) America/Rio_Branco"),
                    ("America/Santarem", "(GMT-0300) America/Santarem"),
                    ("America/Santiago", "(GMT-0300) America/Santiago"),
                    ("America/Santo_Domingo", "(GMT-0400) America/Santo_Domingo"),
                    ("America/Sao_Paulo", "(GMT-0300) America/Sao_Paulo"),
                    ("America/Scoresbysund", "(GMT-0100) America/Scoresbysund"),
                    ("America/Sitka", "(GMT-0900) America/Sitka"),
                    ("America/St_Barthelemy", "(GMT-0400) America/St_Barthelemy"),
                    ("America/St_Johns", "(GMT-0330) America/St_Johns"),
                    ("America/St_Kitts", "(GMT-0400) America/St_Kitts"),
                    ("America/St_Lucia", "(GMT-0400) America/St_Lucia"),
                    ("America/St_Thomas", "(GMT-0400) America/St_Thomas"),
                    ("America/St_Vincent", "(GMT-0400) America/St_Vincent"),
                    ("America/Swift_Current", "(GMT-0600) America/Swift_Current"),
                    ("America/Tegucigalpa", "(GMT-0600) America/Tegucigalpa"),
                    ("America/Thule", "(GMT-0400) America/Thule"),
                    ("America/Thunder_Bay", "(GMT-0500) America/Thunder_Bay"),
                    ("America/Tijuana", "(GMT-0800) America/Tijuana"),
                    ("America/Toronto", "(GMT-0500) America/Toronto"),
                    ("America/Tortola", "(GMT-0400) America/Tortola"),
                    ("America/Vancouver", "(GMT-0800) America/Vancouver"),
                    ("America/Whitehorse", "(GMT-0700) America/Whitehorse"),
                    ("America/Winnipeg", "(GMT-0600) America/Winnipeg"),
                    ("America/Yakutat", "(GMT-0900) America/Yakutat"),
                    ("America/Yellowknife", "(GMT-0700) America/Yellowknife"),
                    ("Antarctica/Casey", "(GMT+1100) Antarctica/Casey"),
                    ("Antarctica/Davis", "(GMT+0700) Antarctica/Davis"),
                    ("Antarctica/DumontDUrville", "(GMT+1000) Antarctica/DumontDUrville"),
                    ("Antarctica/Macquarie", "(GMT+1100) Antarctica/Macquarie"),
                    ("Antarctica/Mawson", "(GMT+0500) Antarctica/Mawson"),
                    ("Antarctica/McMurdo", "(GMT+1300) Antarctica/McMurdo"),
                    ("Antarctica/Palmer", "(GMT-0300) Antarctica/Palmer"),
                    ("Antarctica/Rothera", "(GMT-0300) Antarctica/Rothera"),
                    ("Antarctica/Syowa", "(GMT+0300) Antarctica/Syowa"),
                    ("Antarctica/Troll", "(GMT+0000) Antarctica/Troll"),
                    ("Antarctica/Vostok", "(GMT+0600) Antarctica/Vostok"),
                    ("Arctic/Longyearbyen", "(GMT+0100) Arctic/Longyearbyen"),
                    ("Asia/Aden", "(GMT+0300) Asia/Aden"),
                    ("Asia/Almaty", "(GMT+0600) Asia/Almaty"),
                    ("Asia/Amman", "(GMT+0200) Asia/Amman"),
                    ("Asia/Anadyr", "(GMT+1200) Asia/Anadyr"),
                    ("Asia/Aqtau", "(GMT+0500) Asia/Aqtau"),
                    ("Asia/Aqtobe", "(GMT+0500) Asia/Aqtobe"),
                    ("Asia/Ashgabat", "(GMT+0500) Asia/Ashgabat"),
                    ("Asia/Atyrau", "(GMT+0500) Asia/Atyrau"),
                    ("Asia/Baghdad", "(GMT+0300) Asia/Baghdad"),
                    ("Asia/Bahrain", "(GMT+0300) Asia/Bahrain"),
                    ("Asia/Baku", "(GMT+0400) Asia/Baku"),
                    ("Asia/Bangkok", "(GMT+0700) Asia/Bangkok"),
                    ("Asia/Barnaul", "(GMT+0700) Asia/Barnaul"),
                    ("Asia/Beirut", "(GMT+0200) Asia/Beirut"),
                    ("Asia/Bishkek", "(GMT+0600) Asia/Bishkek"),
                    ("Asia/Brunei", "(GMT+0800) Asia/Brunei"),
                    ("Asia/Chita", "(GMT+0900) Asia/Chita"),
                    ("Asia/Choibalsan", "(GMT+0800) Asia/Choibalsan"),
                    ("Asia/Colombo", "(GMT+0530) Asia/Colombo"),
                    ("Asia/Damascus", "(GMT+0200) Asia/Damascus"),
                    ("Asia/Dhaka", "(GMT+0600) Asia/Dhaka"),
                    ("Asia/Dili", "(GMT+0900) Asia/Dili"),
                    ("Asia/Dubai", "(GMT+0400) Asia/Dubai"),
                    ("Asia/Dushanbe", "(GMT+0500) Asia/Dushanbe"),
                    ("Asia/Famagusta", "(GMT+0200) Asia/Famagusta"),
                    ("Asia/Gaza", "(GMT+0200) Asia/Gaza"),
                    ("Asia/Hebron", "(GMT+0200) Asia/Hebron"),
                    ("Asia/Ho_Chi_Minh", "(GMT+0700) Asia/Ho_Chi_Minh"),
                    ("Asia/Hong_Kong", "(GMT+0800) Asia/Hong_Kong"),
                    ("Asia/Hovd", "(GMT+0700) Asia/Hovd"),
                    ("Asia/Irkutsk", "(GMT+0800) Asia/Irkutsk"),
                    ("Asia/Jakarta", "(GMT+0700) Asia/Jakarta"),
                    ("Asia/Jayapura", "(GMT+0900) Asia/Jayapura"),
                    ("Asia/Jerusalem", "(GMT+0200) Asia/Jerusalem"),
                    ("Asia/Kabul", "(GMT+0430) Asia/Kabul"),
                    ("Asia/Kamchatka", "(GMT+1200) Asia/Kamchatka"),
                    ("Asia/Karachi", "(GMT+0500) Asia/Karachi"),
                    ("Asia/Kathmandu", "(GMT+0545) Asia/Kathmandu"),
                    ("Asia/Khandyga", "(GMT+0900) Asia/Khandyga"),
                    ("Asia/Kolkata", "(GMT+0530) Asia/Kolkata"),
                    ("Asia/Krasnoyarsk", "(GMT+0700) Asia/Krasnoyarsk"),
                    ("Asia/Kuala_Lumpur", "(GMT+0800) Asia/Kuala_Lumpur"),
                    ("Asia/Kuching", "(GMT+0800) Asia/Kuching"),
                    ("Asia/Kuwait", "(GMT+0300) Asia/Kuwait"),
                    ("Asia/Macau", "(GMT+0800) Asia/Macau"),
                    ("Asia/Magadan", "(GMT+1100) Asia/Magadan"),
                    ("Asia/Makassar", "(GMT+0800) Asia/Makassar"),
                    ("Asia/Manila", "(GMT+0800) Asia/Manila"),
                    ("Asia/Muscat", "(GMT+0400) Asia/Muscat"),
                    ("Asia/Nicosia", "(GMT+0200) Asia/Nicosia"),
                    ("Asia/Novokuznetsk", "(GMT+0700) Asia/Novokuznetsk"),
                    ("Asia/Novosibirsk", "(GMT+0700) Asia/Novosibirsk"),
                    ("Asia/Omsk", "(GMT+0600) Asia/Omsk"),
                    ("Asia/Oral", "(GMT+0500) Asia/Oral"),
                    ("Asia/Phnom_Penh", "(GMT+0700) Asia/Phnom_Penh"),
                    ("Asia/Pontianak", "(GMT+0700) Asia/Pontianak"),
                    ("Asia/Pyongyang", "(GMT+0900) Asia/Pyongyang"),
                    ("Asia/Qatar", "(GMT+0300) Asia/Qatar"),
                    ("Asia/Qostanay", "(GMT+0600) Asia/Qostanay"),
                    ("Asia/Qyzylorda", "(GMT+0500) Asia/Qyzylorda"),
                    ("Asia/Riyadh", "(GMT+0300) Asia/Riyadh"),
                    ("Asia/Sakhalin", "(GMT+1100) Asia/Sakhalin"),
                    ("Asia/Samarkand", "(GMT+0500) Asia/Samarkand"),
                    ("Asia/Seoul", "(GMT+0900) Asia/Seoul"),
                    ("Asia/Shanghai", "(GMT+0800) Asia/Shanghai"),
                    ("Asia/Singapore", "(GMT+0800) Asia/Singapore"),
                    ("Asia/Srednekolymsk", "(GMT+1100) Asia/Srednekolymsk"),
                    ("Asia/Taipei", "(GMT+0800) Asia/Taipei"),
                    ("Asia/Tashkent", "(GMT+0500) Asia/Tashkent"),
                    ("Asia/Tbilisi", "(GMT+0400) Asia/Tbilisi"),
                    ("Asia/Tehran", "(GMT+0330) Asia/Tehran"),
                    ("Asia/Thimphu", "(GMT+0600) Asia/Thimphu"),
                    ("Asia/Tokyo", "(GMT+0900) Asia/Tokyo"),
                    ("Asia/Tomsk", "(GMT+0700) Asia/Tomsk"),
                    ("Asia/Ulaanbaatar", "(GMT+0800) Asia/Ulaanbaatar"),
                    ("Asia/Urumqi", "(GMT+0600) Asia/Urumqi"),
                    ("Asia/Ust-Nera", "(GMT+1000) Asia/Ust-Nera"),
                    ("Asia/Vientiane", "(GMT+0700) Asia/Vientiane"),
                    ("Asia/Vladivostok", "(GMT+1000) Asia/Vladivostok"),
                    ("Asia/Yakutsk", "(GMT+0900) Asia/Yakutsk"),
                    ("Asia/Yangon", "(GMT+0630) Asia/Yangon"),
                    ("Asia/Yekaterinburg", "(GMT+0500) Asia/Yekaterinburg"),
                    ("Asia/Yerevan", "(GMT+0400) Asia/Yerevan"),
                    ("Atlantic/Azores", "(GMT-0100) Atlantic/Azores"),
                    ("Atlantic/Bermuda", "(GMT-0400) Atlantic/Bermuda"),
                    ("Atlantic/Canary", "(GMT+0000) Atlantic/Canary"),
                    ("Atlantic/Cape_Verde", "(GMT-0100) Atlantic/Cape_Verde"),
                    ("Atlantic/Faroe", "(GMT+0000) Atlantic/Faroe"),
                    ("Atlantic/Madeira", "(GMT+0000) Atlantic/Madeira"),
                    ("Atlantic/Reykjavik", "(GMT+0000) Atlantic/Reykjavik"),
                    ("Atlantic/South_Georgia", "(GMT-0200) Atlantic/South_Georgia"),
                    ("Atlantic/St_Helena", "(GMT+0000) Atlantic/St_Helena"),
                    ("Atlantic/Stanley", "(GMT-0300) Atlantic/Stanley"),
                    ("Australia/Adelaide", "(GMT+1030) Australia/Adelaide"),
                    ("Australia/Brisbane", "(GMT+1000) Australia/Brisbane"),
                    ("Australia/Broken_Hill", "(GMT+1030) Australia/Broken_Hill"),
                    ("Australia/Currie", "(GMT+1100) Australia/Currie"),
                    ("Australia/Darwin", "(GMT+0930) Australia/Darwin"),
                    ("Australia/Eucla", "(GMT+0845) Australia/Eucla"),
                    ("Australia/Hobart", "(GMT+1100) Australia/Hobart"),
                    ("Australia/Lindeman", "(GMT+1000) Australia/Lindeman"),
                    ("Australia/Lord_Howe", "(GMT+1100) Australia/Lord_Howe"),
                    ("Australia/Melbourne", "(GMT+1100) Australia/Melbourne"),
                    ("Australia/Perth", "(GMT+0800) Australia/Perth"),
                    ("Australia/Sydney", "(GMT+1100) Australia/Sydney"),
                    ("Canada/Atlantic", "(GMT-0400) Canada/Atlantic"),
                    ("Canada/Central", "(GMT-0600) Canada/Central"),
                    ("Canada/Eastern", "(GMT-0500) Canada/Eastern"),
                    ("Canada/Mountain", "(GMT-0700) Canada/Mountain"),
                    ("Canada/Newfoundland", "(GMT-0330) Canada/Newfoundland"),
                    ("Canada/Pacific", "(GMT-0800) Canada/Pacific"),
                    ("Europe/Amsterdam", "(GMT+0100) Europe/Amsterdam"),
                    ("Europe/Andorra", "(GMT+0100) Europe/Andorra"),
                    ("Europe/Astrakhan", "(GMT+0400) Europe/Astrakhan"),
                    ("Europe/Athens", "(GMT+0200) Europe/Athens"),
                    ("Europe/Belgrade", "(GMT+0100) Europe/Belgrade"),
                    ("Europe/Berlin", "(GMT+0100) Europe/Berlin"),
                    ("Europe/Bratislava", "(GMT+0100) Europe/Bratislava"),
                    ("Europe/Brussels", "(GMT+0100) Europe/Brussels"),
                    ("Europe/Bucharest", "(GMT+0200) Europe/Bucharest"),
                    ("Europe/Budapest", "(GMT+0100) Europe/Budapest"),
                    ("Europe/Busingen", "(GMT+0100) Europe/Busingen"),
                    ("Europe/Chisinau", "(GMT+0200) Europe/Chisinau"),
                    ("Europe/Copenhagen", "(GMT+0100) Europe/Copenhagen"),
                    ("Europe/Dublin", "(GMT+0000) Europe/Dublin"),
                    ("Europe/Gibraltar", "(GMT+0100) Europe/Gibraltar"),
                    ("Europe/Guernsey", "(GMT+0000) Europe/Guernsey"),
                    ("Europe/Helsinki", "(GMT+0200) Europe/Helsinki"),
                    ("Europe/Isle_of_Man", "(GMT+0000) Europe/Isle_of_Man"),
                    ("Europe/Istanbul", "(GMT+0300) Europe/Istanbul"),
                    ("Europe/Jersey", "(GMT+0000) Europe/Jersey"),
                    ("Europe/Kaliningrad", "(GMT+0200) Europe/Kaliningrad"),
                    ("Europe/Kiev", "(GMT+0200) Europe/Kiev"),
                    ("Europe/Kirov", "(GMT+0300) Europe/Kirov"),
                    ("Europe/Lisbon", "(GMT+0000) Europe/Lisbon"),
                    ("Europe/Ljubljana", "(GMT+0100) Europe/Ljubljana"),
                    ("Europe/London", "(GMT+0000) Europe/London"),
                    ("Europe/Luxembourg", "(GMT+0100) Europe/Luxembourg"),
                    ("Europe/Madrid", "(GMT+0100) Europe/Madrid"),
                    ("Europe/Malta", "(GMT+0100) Europe/Malta"),
                    ("Europe/Mariehamn", "(GMT+0200) Europe/Mariehamn"),
                    ("Europe/Minsk", "(GMT+0300) Europe/Minsk"),
                    ("Europe/Monaco", "(GMT+0100) Europe/Monaco"),
                    ("Europe/Moscow", "(GMT+0300) Europe/Moscow"),
                    ("Europe/Oslo", "(GMT+0100) Europe/Oslo"),
                    ("Europe/Paris", "(GMT+0100) Europe/Paris"),
                    ("Europe/Podgorica", "(GMT+0100) Europe/Podgorica"),
                    ("Europe/Prague", "(GMT+0100) Europe/Prague"),
                    ("Europe/Riga", "(GMT+0200) Europe/Riga"),
                    ("Europe/Rome", "(GMT+0100) Europe/Rome"),
                    ("Europe/Samara", "(GMT+0400) Europe/Samara"),
                    ("Europe/San_Marino", "(GMT+0100) Europe/San_Marino"),
                    ("Europe/Sarajevo", "(GMT+0100) Europe/Sarajevo"),
                    ("Europe/Saratov", "(GMT+0400) Europe/Saratov"),
                    ("Europe/Simferopol", "(GMT+0300) Europe/Simferopol"),
                    ("Europe/Skopje", "(GMT+0100) Europe/Skopje"),
                    ("Europe/Sofia", "(GMT+0200) Europe/Sofia"),
                    ("Europe/Stockholm", "(GMT+0100) Europe/Stockholm"),
                    ("Europe/Tallinn", "(GMT+0200) Europe/Tallinn"),
                    ("Europe/Tirane", "(GMT+0100) Europe/Tirane"),
                    ("Europe/Ulyanovsk", "(GMT+0400) Europe/Ulyanovsk"),
                    ("Europe/Uzhgorod", "(GMT+0200) Europe/Uzhgorod"),
                    ("Europe/Vaduz", "(GMT+0100) Europe/Vaduz"),
                    ("Europe/Vatican", "(GMT+0100) Europe/Vatican"),
                    ("Europe/Vienna", "(GMT+0100) Europe/Vienna"),
                    ("Europe/Vilnius", "(GMT+0200) Europe/Vilnius"),
                    ("Europe/Volgograd", "(GMT+0400) Europe/Volgograd"),
                    ("Europe/Warsaw", "(GMT+0100) Europe/Warsaw"),
                    ("Europe/Zagreb", "(GMT+0100) Europe/Zagreb"),
                    ("Europe/Zaporozhye", "(GMT+0200) Europe/Zaporozhye"),
                    ("Europe/Zurich", "(GMT+0100) Europe/Zurich"),
                    ("GMT", "(GMT+0000) GMT"),
                    ("Indian/Antananarivo", "(GMT+0300) Indian/Antananarivo"),
                    ("Indian/Chagos", "(GMT+0600) Indian/Chagos"),
                    ("Indian/Christmas", "(GMT+0700) Indian/Christmas"),
                    ("Indian/Cocos", "(GMT+0630) Indian/Cocos"),
                    ("Indian/Comoro", "(GMT+0300) Indian/Comoro"),
                    ("Indian/Kerguelen", "(GMT+0500) Indian/Kerguelen"),
                    ("Indian/Mahe", "(GMT+0400) Indian/Mahe"),
                    ("Indian/Maldives", "(GMT+0500) Indian/Maldives"),
                    ("Indian/Mauritius", "(GMT+0400) Indian/Mauritius"),
                    ("Indian/Mayotte", "(GMT+0300) Indian/Mayotte"),
                    ("Indian/Reunion", "(GMT+0400) Indian/Reunion"),
                    ("Pacific/Apia", "(GMT+1400) Pacific/Apia"),
                    ("Pacific/Auckland", "(GMT+1300) Pacific/Auckland"),
                    ("Pacific/Bougainville", "(GMT+1100) Pacific/Bougainville"),
                    ("Pacific/Chatham", "(GMT+1345) Pacific/Chatham"),
                    ("Pacific/Chuuk", "(GMT+1000) Pacific/Chuuk"),
                    ("Pacific/Easter", "(GMT-0500) Pacific/Easter"),
                    ("Pacific/Efate", "(GMT+1100) Pacific/Efate"),
                    ("Pacific/Enderbury", "(GMT+1300) Pacific/Enderbury"),
                    ("Pacific/Fakaofo", "(GMT+1300) Pacific/Fakaofo"),
                    ("Pacific/Fiji", "(GMT+1300) Pacific/Fiji"),
                    ("Pacific/Funafuti", "(GMT+1200) Pacific/Funafuti"),
                    ("Pacific/Galapagos", "(GMT-0600) Pacific/Galapagos"),
                    ("Pacific/Gambier", "(GMT-0900) Pacific/Gambier"),
                    ("Pacific/Guadalcanal", "(GMT+1100) Pacific/Guadalcanal"),
                    ("Pacific/Guam", "(GMT+1000) Pacific/Guam"),
                    ("Pacific/Honolulu", "(GMT-1000) Pacific/Honolulu"),
                    ("Pacific/Kiritimati", "(GMT+1400) Pacific/Kiritimati"),
                    ("Pacific/Kosrae", "(GMT+1100) Pacific/Kosrae"),
                    ("Pacific/Kwajalein", "(GMT+1200) Pacific/Kwajalein"),
                    ("Pacific/Majuro", "(GMT+1200) Pacific/Majuro"),
                    ("Pacific/Marquesas", "(GMT-0930) Pacific/Marquesas"),
                    ("Pacific/Midway", "(GMT-1100) Pacific/Midway"),
                    ("Pacific/Nauru", "(GMT+1200) Pacific/Nauru"),
                    ("Pacific/Niue", "(GMT-1100) Pacific/Niue"),
                    ("Pacific/Norfolk", "(GMT+1200) Pacific/Norfolk"),
                    ("Pacific/Noumea", "(GMT+1100) Pacific/Noumea"),
                    ("Pacific/Pago_Pago", "(GMT-1100) Pacific/Pago_Pago"),
                    ("Pacific/Palau", "(GMT+0900) Pacific/Palau"),
                    ("Pacific/Pitcairn", "(GMT-0800) Pacific/Pitcairn"),
                    ("Pacific/Pohnpei", "(GMT+1100) Pacific/Pohnpei"),
                    ("Pacific/Port_Moresby", "(GMT+1000) Pacific/Port_Moresby"),
                    ("Pacific/Rarotonga", "(GMT-1000) Pacific/Rarotonga"),
                    ("Pacific/Saipan", "(GMT+1000) Pacific/Saipan"),
                    ("Pacific/Tahiti", "(GMT-1000) Pacific/Tahiti"),
                    ("Pacific/Tarawa", "(GMT+1200) Pacific/Tarawa"),
                    ("Pacific/Tongatapu", "(GMT+1300) Pacific/Tongatapu"),
                    ("Pacific/Wake", "(GMT+1200) Pacific/Wake"),
                    ("Pacific/Wallis", "(GMT+1200) Pacific/Wallis"),
                    ("US/Alaska", "(GMT-0900) US/Alaska"),
                    ("US/Arizona", "(GMT-0700) US/Arizona"),
                    ("US/Central", "(GMT-0600) US/Central"),
                    ("US/Eastern", "(GMT-0500) US/Eastern"),
                    ("US/Hawaii", "(GMT-1000) US/Hawaii"),
                    ("US/Mountain", "(GMT-0700) US/Mountain"),
                    ("US/Pacific", "(GMT-0800) US/Pacific"),
                    ("UTC", "(GMT+0000) UTC"),
                ],
                default="America/New_York",
                max_length=100,
            ),
        ),
    ]