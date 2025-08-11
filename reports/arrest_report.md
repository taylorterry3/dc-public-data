# DC Metropolitan Police Department Adult Arrest Trends, 2023-2024

## Background

MPD recently made its annual public release of adult arrest data, covering 19,263 arrests in 2024. This data represents the first full year of data available since Chief Smith took office in November of 2023, and reveals major changes in policing strategy over that timeframe.

This brief report includes a few pages of analysis of trends citywide and by Ward, focused on changes from 2023 to 2024. The rest of the pages are a series of appendices with a tables and chart of arrest trends for each Ward, Police District, ANC, and PSA for those who want to see a more local view.

This adult arrest data is taken from the Open Data DC website. DC resident and data scientist Taylor Terry maintains an archive of this and other DC public data at https://github.com/taylorterry3/dc-public-data. The code used to generate this report is also available in that repository. This version of the report was generated on April 25, 2025. This report, including any updated versions, is available in Google Drive at bit.ly/4iG0Uht.

Taylor can be reached at taylor.terry@gmail.com.


### Citywide Changes in Arrest Patterns

In 2024 MPD made 19,263 adult arrests citywide, a +27% change from 15,223 arrests in 2023 and a +30% change from the 2021-2023 average of 14,861. The increase in arrests was concentrated in Wards 1, 7, and 8. These wards each saw more than 1,000 additional arrests, while the next biggest gain was 212 additional arrests in Ward 5.

| Ward | 2023 | 2024 | Change | Percent Change |
|------|------:|------:|--------:|---------------:|
| 1 | 1,699 | 2,820 | +1,121 | +66% |
| 2 | 1,790 | 1,916 | +126 | +7% |
| 3 | 466 | 477 | +11 | +2% |
| 4 | 1,119 | 1,296 | +177 | +16% |
| 5 | 2,414 | 2,626 | +212 | +9% |
| 6 | 1,578 | 1,723 | +145 | +9% |
| 7 | 2,798 | 4,017 | +1,219 | +44% |
| 8 | 3,359 | 4,388 | +1,029 | +31% |

\newpage

Much of this increase in arrests was driven by 2,000 additional arrests for Traffic Violations, 868 more for Theft, 814 more for Narcotics, and 743 more for Liquor Law Violations. 

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 898 | 2,898 | +2,000 | +223% |
| Theft | 870 | 1,738 | +868 | +100% |
| Narcotics | 529 | 1,343 | +814 | +154% |
| Liquor Law Violations | 164 | 907 | +743 | +453% |
| All Other Categories | 12,762 | 12,377 | -385 | -3% |

\newpage

This crosstab shows the percentage change for these arrest categories by Ward from 2023 to 2024. Note especially the roughly tenfold increase in Liquor Law Violation arrests in Wards 7 and 8, as well as a similarly large increase in Traffic Violation arrests in Ward 7. Ward 1 saw fivefold increases in Liquor Law Violation and Narcotics arrests, while Ward 5 saw a similar rate of increase in Liquor Law Violation Arrests. 

|Category| W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 |
|--------|---:|---:|---:|---:|---:|---:|---:|----:|
| Traffic | +108% | +45% | +106% | +80% | +129% | +137% | +1047% | +211% |
| Theft | +176% | +69% | +16% | +231% | +56% | +79% | +173% | +89% |
| Narcotics | +400% | +42% | +33% | -29% | +113% | +181% | +100% | +229% |
| Liquor | +433% | +89% | +100% | +260% | +470% | +140% | +844% | +1369% |
| Other | +23% | -10% | -7% | 0% | -13% | -11% | -10% | +4% |

### Productivity per Officer

MPD reported having 3,282 sworn officers in 2024, meaning that 19,263 arrests represents 5.9 arrests per sworn officer for the year. This is a substantial increase from the 2021-2023 average of 4.3 arrests per officer per year, but is far from a return to the 2016-2019 average of 7.7 arrests per officer. 

The chart below shows the trend in arrests per sworn officer per month over time, as well as the trend in stops per officer for periods when this data is available. MPD stops data currently runs only from 2019 through June of 2024. The release schedule is irregular and MPD has historically refused to release this data in response to FOIA requests, and so it is unclear when the rest of the 2024 data will be available. 

![](images/citywide_officer_trends.png)



\newpage
### Arrests by Category

The table below shows the number of arrests by category citywide for the years 2023 and 2024, sorted by percentage change. Of particular note is that DWI arrests remained flat despite a greater than threefold increase in arrests for Traffic Violations. 

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 164 | 907 | +743 | +453% |
| Traffic Violations | 898 | 2,898 | +2,000 | +223% |
| Narcotics | 529 | 1,343 | +814 | +154% |
| Theft from Auto | 14 | 30 | +16 | +114% |
| Prostitution | 10 | 20 | +10 | +100% |
| Theft | 870 | 1,738 | +868 | +100% |
| Aggravated Assault | 122 | 236 | +114 | +93% |
| Disorderly Conduct | 106 | 195 | +89 | +84% |
| Motor Vehicle Theft | 31 | 50 | +19 | +61% |
| Gambling | 5 | 7 | +2 | +40% |
| Fraud and Financial Crimes | 25 | 34 | +9 | +36% |
| Burglary | 113 | 148 | +35 | +31% |
| Robbery | 181 | 223 | +42 | +23% |
| Assault with a Dangerous Weapon | 398 | 433 | +35 | +9% |
| Assault on a Police Officer | 298 | 320 | +22 | +7% |
| Release Violations/Fugitive | 1,568 | 1,610 | +42 | +3% |
| Arson | 6 | 6 | +0 | 0% |
| Driving/Boating While Intoxicated | 606 | 604 | -2 | 0% |
| Property Crimes | 493 | 491 | -2 | 0% |
| Sex Offenses | 128 | 124 | -4 | -3% |
| Other Crimes | 1,043 | 976 | -67 | -6% |
| Offenses Against Family & Children | 391 | 361 | -30 | -8% |
| Simple Assault | 5,002 | 4,570 | -432 | -9% |
| Weapon Violations | 1,421 | 1,286 | -135 | -10% |
| Homicide | 96 | 83 | -13 | -14% |
| Damage to Property | 627 | 527 | -100 | -16% |
| Sex Abuse | 54 | 35 | -19 | -35% |
| Kidnapping | 16 | 8 | -8 | -50% |
| Vending Violations | 8 | 0 | -8 | -100% |

\newpage

This chart presents the same data as above in a visual format, sorted by arrest category.

![](images/citywide_categories.png)



\newpage
# Appendix 1: Data by Ward



## Ward 1

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Motor Vehicle Theft | 1 | 7 | +6 | +600% |
| Liquor Law Violations | 39 | 208 | +169 | +433% |
| Narcotics | 53 | 265 | +212 | +400% |
| Theft | 185 | 510 | +325 | +176% |
| Disorderly Conduct | 31 | 80 | +49 | +158% |
| Theft from Auto | 4 | 9 | +5 | +125% |
| Traffic Violations | 106 | 220 | +114 | +108% |
| Robbery | 23 | 47 | +24 | +104% |
| Release Violations/Fugitive | 128 | 235 | +107 | +84% |
| Sex Abuse | 4 | 7 | +3 | +75% |
| Aggravated Assault | 16 | 26 | +10 | +62% |
| Burglary | 17 | 24 | +7 | +41% |
| Weapon Violations | 150 | 189 | +39 | +26% |
| Assault on a Police Officer | 43 | 51 | +8 | +19% |
| Damage to Property | 55 | 62 | +7 | +13% |
| Property Crimes | 35 | 39 | +4 | +11% |
| Simple Assault | 454 | 504 | +50 | +11% |
| Driving/Boating While Intoxicated | 67 | 73 | +6 | +9% |
| Other Crimes | 170 | 176 | +6 | +4% |
| Gambling | 2 | 2 | +0 | 0% |
| Offenses Against Family & Children | 32 | 28 | -4 | -12% |
| Assault with a Dangerous Weapon | 54 | 40 | -14 | -26% |
| Sex Offenses | 20 | 14 | -6 | -30% |
| Fraud and Financial Crimes | 4 | 2 | -2 | -50% |
| Kidnapping | 2 | 1 | -1 | -50% |
| Homicide | 3 | 1 | -2 | -67% |
| Arson | 1 | 0 | -1 | -100% |
| Prostitution | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/ward_1_categories.png)



\newpage
## Ward 2

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Robbery | 12 | 25 | +13 | +108% |
| Liquor Law Violations | 44 | 83 | +39 | +89% |
| Theft | 177 | 300 | +123 | +69% |
| Traffic Violations | 152 | 221 | +69 | +45% |
| Narcotics | 66 | 94 | +28 | +42% |
| Aggravated Assault | 9 | 12 | +3 | +33% |
| Offenses Against Family & Children | 17 | 22 | +5 | +29% |
| Driving/Boating While Intoxicated | 76 | 98 | +22 | +29% |
| Assault on a Police Officer | 38 | 44 | +6 | +16% |
| Assault with a Dangerous Weapon | 28 | 32 | +4 | +14% |
| Other Crimes | 147 | 150 | +3 | +2% |
| Theft from Auto | 1 | 1 | +0 | 0% |
| Damage to Property | 56 | 53 | -3 | -5% |
| Simple Assault | 456 | 410 | -46 | -10% |
| Release Violations/Fugitive | 173 | 145 | -28 | -16% |
| Disorderly Conduct | 28 | 22 | -6 | -21% |
| Homicide | 4 | 3 | -1 | -25% |
| Burglary | 11 | 8 | -3 | -27% |
| Weapon Violations | 193 | 130 | -63 | -33% |
| Property Crimes | 57 | 37 | -20 | -35% |
| Sex Abuse | 5 | 3 | -2 | -40% |
| Sex Offenses | 17 | 9 | -8 | -47% |
| Fraud and Financial Crimes | 11 | 5 | -6 | -55% |
| Motor Vehicle Theft | 6 | 2 | -4 | -67% |
| Arson | 1 | 0 | -1 | -100% |
| Gambling | 3 | 0 | -3 | -100% |
| Kidnapping | 1 | 0 | -1 | -100% |
| Vending Violations | 1 | 0 | -1 | -100% |
| Prostitution | 0 | 7 | +7 | N/A |

![](images/ward_2_categories.png)



\newpage
## Ward 3

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Assault on a Police Officer | 4 | 11 | +7 | +175% |
| Aggravated Assault | 2 | 5 | +3 | +150% |
| Traffic Violations | 17 | 35 | +18 | +106% |
| Disorderly Conduct | 1 | 2 | +1 | +100% |
| Liquor Law Violations | 1 | 2 | +1 | +100% |
| Sex Abuse | 1 | 2 | +1 | +100% |
| Sex Offenses | 5 | 7 | +2 | +40% |
| Narcotics | 3 | 4 | +1 | +33% |
| Driving/Boating While Intoxicated | 16 | 20 | +4 | +25% |
| Theft | 92 | 107 | +15 | +16% |
| Release Violations/Fugitive | 40 | 43 | +3 | +8% |
| Weapon Violations | 12 | 12 | +0 | 0% |
| Other Crimes | 36 | 34 | -2 | -6% |
| Offenses Against Family & Children | 13 | 12 | -1 | -8% |
| Damage to Property | 21 | 19 | -2 | -10% |
| Simple Assault | 158 | 133 | -25 | -16% |
| Assault with a Dangerous Weapon | 16 | 12 | -4 | -25% |
| Robbery | 9 | 6 | -3 | -33% |
| Theft from Auto | 3 | 2 | -1 | -33% |
| Property Crimes | 5 | 3 | -2 | -40% |
| Burglary | 6 | 3 | -3 | -50% |
| Motor Vehicle Theft | 2 | 1 | -1 | -50% |
| Arson | 1 | 0 | -1 | -100% |
| Vending Violations | 2 | 0 | -2 | -100% |
| Fraud and Financial Crimes | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 1 | +1 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |

![](images/ward_3_categories.png)



\newpage
## Ward 4

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Fraud and Financial Crimes | 1 | 7 | +6 | +600% |
| Disorderly Conduct | 2 | 8 | +6 | +300% |
| Liquor Law Violations | 5 | 18 | +13 | +260% |
| Theft | 35 | 116 | +81 | +231% |
| Motor Vehicle Theft | 2 | 5 | +3 | +150% |
| Traffic Violations | 122 | 220 | +98 | +80% |
| Sex Offenses | 6 | 10 | +4 | +67% |
| Burglary | 8 | 11 | +3 | +38% |
| Driving/Boating While Intoxicated | 65 | 77 | +12 | +18% |
| Robbery | 13 | 15 | +2 | +15% |
| Assault with a Dangerous Weapon | 21 | 24 | +3 | +14% |
| Property Crimes | 29 | 33 | +4 | +14% |
| Release Violations/Fugitive | 121 | 136 | +15 | +12% |
| Simple Assault | 360 | 370 | +10 | +3% |
| Aggravated Assault | 12 | 11 | -1 | -8% |
| Other Crimes | 88 | 74 | -14 | -16% |
| Damage to Property | 49 | 39 | -10 | -20% |
| Assault on a Police Officer | 14 | 10 | -4 | -29% |
| Narcotics | 48 | 34 | -14 | -29% |
| Offenses Against Family & Children | 34 | 24 | -10 | -29% |
| Weapon Violations | 76 | 50 | -26 | -34% |
| Homicide | 4 | 1 | -3 | -75% |
| Sex Abuse | 4 | 1 | -3 | -75% |
| Arson | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 2 | +2 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/ward_4_categories.png)



\newpage
## Ward 5

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 20 | 114 | +94 | +470% |
| Theft from Auto | 2 | 6 | +4 | +200% |
| Aggravated Assault | 20 | 48 | +28 | +140% |
| Traffic Violations | 163 | 373 | +210 | +129% |
| Narcotics | 77 | 164 | +87 | +113% |
| Fraud and Financial Crimes | 3 | 6 | +3 | +100% |
| Motor Vehicle Theft | 7 | 11 | +4 | +57% |
| Theft | 147 | 229 | +82 | +56% |
| Disorderly Conduct | 17 | 21 | +4 | +24% |
| Driving/Boating While Intoxicated | 94 | 105 | +11 | +12% |
| Robbery | 33 | 36 | +3 | +9% |
| Kidnapping | 2 | 2 | +0 | 0% |
| Offenses Against Family & Children | 45 | 45 | +0 | 0% |
| Release Violations/Fugitive | 247 | 230 | -17 | -7% |
| Assault with a Dangerous Weapon | 61 | 55 | -6 | -10% |
| Sex Offenses | 17 | 15 | -2 | -12% |
| Simple Assault | 833 | 698 | -135 | -16% |
| Weapon Violations | 178 | 143 | -35 | -20% |
| Property Crimes | 80 | 64 | -16 | -20% |
| Burglary | 24 | 19 | -5 | -21% |
| Damage to Property | 103 | 77 | -26 | -25% |
| Homicide | 10 | 7 | -3 | -30% |
| Other Crimes | 172 | 117 | -55 | -32% |
| Assault on a Police Officer | 52 | 35 | -17 | -33% |
| Sex Abuse | 6 | 4 | -2 | -33% |
| Vending Violations | 1 | 0 | -1 | -100% |
| Arson | 0 | 2 | +2 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |

![](images/ward_5_categories.png)



\newpage
## Ward 6

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 47 | 132 | +85 | +181% |
| Liquor Law Violations | 15 | 36 | +21 | +140% |
| Traffic Violations | 78 | 185 | +107 | +137% |
| Arson | 1 | 2 | +1 | +100% |
| Theft | 107 | 192 | +85 | +79% |
| Aggravated Assault | 16 | 28 | +12 | +75% |
| Robbery | 19 | 27 | +8 | +42% |
| Assault with a Dangerous Weapon | 22 | 30 | +8 | +36% |
| Sex Offenses | 19 | 24 | +5 | +26% |
| Weapon Violations | 87 | 92 | +5 | +6% |
| Burglary | 18 | 19 | +1 | +6% |
| Assault on a Police Officer | 30 | 30 | +0 | 0% |
| Disorderly Conduct | 14 | 14 | +0 | 0% |
| Fraud and Financial Crimes | 4 | 4 | +0 | 0% |
| Kidnapping | 1 | 1 | +0 | 0% |
| Motor Vehicle Theft | 5 | 5 | +0 | 0% |
| Property Crimes | 50 | 50 | +0 | 0% |
| Homicide | 37 | 33 | -4 | -11% |
| Release Violations/Fugitive | 156 | 135 | -21 | -13% |
| Simple Assault | 503 | 421 | -82 | -16% |
| Other Crimes | 117 | 97 | -20 | -17% |
| Offenses Against Family & Children | 77 | 62 | -15 | -19% |
| Driving/Boating While Intoxicated | 63 | 46 | -17 | -27% |
| Damage to Property | 75 | 52 | -23 | -31% |
| Theft from Auto | 3 | 2 | -1 | -33% |
| Sex Abuse | 11 | 4 | -7 | -64% |
| Prostitution | 1 | 0 | -1 | -100% |
| Vending Violations | 2 | 0 | -2 | -100% |
| Gambling | 0 | 0 | +0 | N/A |

![](images/ward_6_categories.png)



\newpage
## Ward 7

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 100 | 1,147 | +1,047 | +1047% |
| Liquor Law Violations | 27 | 255 | +228 | +844% |
| Disorderly Conduct | 3 | 12 | +9 | +300% |
| Fraud and Financial Crimes | 1 | 4 | +3 | +300% |
| Theft | 52 | 142 | +90 | +173% |
| Narcotics | 96 | 192 | +96 | +100% |
| Aggravated Assault | 15 | 28 | +13 | +87% |
| Burglary | 17 | 28 | +11 | +65% |
| Assault with a Dangerous Weapon | 104 | 130 | +26 | +25% |
| Motor Vehicle Theft | 4 | 5 | +1 | +25% |
| Sex Offenses | 20 | 23 | +3 | +15% |
| Offenses Against Family & Children | 67 | 72 | +5 | +7% |
| Release Violations/Fugitive | 388 | 402 | +14 | +4% |
| Homicide | 22 | 21 | -1 | -5% |
| Property Crimes | 124 | 117 | -7 | -6% |
| Assault on a Police Officer | 39 | 35 | -4 | -10% |
| Simple Assault | 957 | 844 | -113 | -12% |
| Robbery | 44 | 37 | -7 | -16% |
| Damage to Property | 125 | 99 | -26 | -21% |
| Driving/Boating While Intoxicated | 69 | 52 | -17 | -25% |
| Weapon Violations | 364 | 263 | -101 | -28% |
| Other Crimes | 141 | 97 | -44 | -31% |
| Sex Abuse | 10 | 4 | -6 | -60% |
| Kidnapping | 5 | 0 | -5 | -100% |
| Prostitution | 4 | 0 | -4 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Gambling | 0 | 3 | +3 | N/A |
| Theft from Auto | 0 | 5 | +5 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/ward_7_categories.png)



\newpage
## Ward 8

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 13 | 191 | +178 | +1369% |
| Fraud and Financial Crimes | 1 | 5 | +4 | +400% |
| Disorderly Conduct | 10 | 36 | +26 | +260% |
| Motor Vehicle Theft | 4 | 14 | +10 | +250% |
| Narcotics | 139 | 458 | +319 | +229% |
| Traffic Violations | 160 | 497 | +337 | +211% |
| Burglary | 12 | 36 | +24 | +200% |
| Theft from Auto | 1 | 3 | +2 | +200% |
| Prostitution | 5 | 13 | +8 | +160% |
| Aggravated Assault | 32 | 78 | +46 | +144% |
| Theft | 75 | 142 | +67 | +89% |
| Other Crimes | 172 | 231 | +59 | +34% |
| Assault on a Police Officer | 78 | 104 | +26 | +33% |
| Property Crimes | 113 | 148 | +35 | +31% |
| Assault with a Dangerous Weapon | 92 | 110 | +18 | +20% |
| Weapon Violations | 361 | 407 | +46 | +13% |
| Robbery | 28 | 30 | +2 | +7% |
| Arson | 2 | 2 | +0 | 0% |
| Homicide | 16 | 16 | +0 | 0% |
| Simple Assault | 1,281 | 1,190 | -91 | -7% |
| Sex Offenses | 24 | 22 | -2 | -8% |
| Offenses Against Family & Children | 106 | 96 | -10 | -9% |
| Release Violations/Fugitive | 315 | 284 | -31 | -10% |
| Damage to Property | 143 | 126 | -17 | -12% |
| Driving/Boating While Intoxicated | 156 | 133 | -23 | -15% |
| Kidnapping | 5 | 4 | -1 | -20% |
| Sex Abuse | 13 | 10 | -3 | -23% |
| Vending Violations | 2 | 0 | -2 | -100% |
| Gambling | 0 | 2 | +2 | N/A |

![](images/ward_8_categories.png)



\newpage
# Appendix 2: Data by Police District



## 1D

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Prostitution | 1 | 2 | +1 | +100% |
| Theft | 140 | 270 | +130 | +93% |
| Traffic Violations | 121 | 220 | +99 | +82% |
| Narcotics | 94 | 168 | +74 | +79% |
| Aggravated Assault | 19 | 31 | +12 | +63% |
| Arson | 2 | 3 | +1 | +50% |
| Theft from Auto | 2 | 3 | +1 | +50% |
| Assault with a Dangerous Weapon | 64 | 89 | +25 | +39% |
| Liquor Law Violations | 42 | 54 | +12 | +29% |
| Robbery | 27 | 32 | +5 | +19% |
| Assault on a Police Officer | 32 | 37 | +5 | +16% |
| Fraud and Financial Crimes | 5 | 5 | +0 | 0% |
| Kidnapping | 1 | 1 | +0 | 0% |
| Sex Offenses | 28 | 28 | +0 | 0% |
| Weapon Violations | 97 | 91 | -6 | -6% |
| Burglary | 25 | 23 | -2 | -8% |
| Homicide | 49 | 44 | -5 | -10% |
| Simple Assault | 574 | 506 | -68 | -12% |
| Motor Vehicle Theft | 7 | 6 | -1 | -14% |
| Other Crimes | 124 | 104 | -20 | -16% |
| Offenses Against Family & Children | 93 | 77 | -16 | -17% |
| Release Violations/Fugitive | 398 | 327 | -71 | -18% |
| Property Crimes | 60 | 48 | -12 | -20% |
| Disorderly Conduct | 18 | 14 | -4 | -22% |
| Driving/Boating While Intoxicated | 71 | 53 | -18 | -25% |
| Damage to Property | 93 | 60 | -33 | -35% |
| Sex Abuse | 12 | 6 | -6 | -50% |
| Gambling | 3 | 0 | -3 | -100% |
| Vending Violations | 4 | 0 | -4 | -100% |

![](images/district_1D_categories.png)



\newpage
## 2D

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 6 | 12 | +6 | +100% |
| Theft | 215 | 316 | +101 | +47% |
| Traffic Violations | 117 | 163 | +46 | +39% |
| Aggravated Assault | 8 | 11 | +3 | +38% |
| Assault on a Police Officer | 27 | 33 | +6 | +22% |
| Release Violations/Fugitive | 99 | 112 | +13 | +13% |
| Driving/Boating While Intoxicated | 63 | 67 | +4 | +6% |
| Offenses Against Family & Children | 21 | 21 | +0 | 0% |
| Property Crimes | 24 | 24 | +0 | 0% |
| Theft from Auto | 3 | 3 | +0 | 0% |
| Other Crimes | 142 | 135 | -7 | -5% |
| Damage to Property | 53 | 48 | -5 | -9% |
| Robbery | 15 | 13 | -2 | -13% |
| Assault with a Dangerous Weapon | 35 | 30 | -5 | -14% |
| Simple Assault | 415 | 346 | -69 | -17% |
| Disorderly Conduct | 17 | 13 | -4 | -24% |
| Sex Offenses | 17 | 13 | -4 | -24% |
| Weapon Violations | 140 | 86 | -54 | -39% |
| Fraud and Financial Crimes | 11 | 6 | -5 | -45% |
| Burglary | 15 | 8 | -7 | -47% |
| Narcotics | 14 | 5 | -9 | -64% |
| Sex Abuse | 6 | 2 | -4 | -67% |
| Motor Vehicle Theft | 7 | 2 | -5 | -71% |
| Arson | 1 | 0 | -1 | -100% |
| Kidnapping | 1 | 0 | -1 | -100% |
| Vending Violations | 3 | 0 | -3 | -100% |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 2 | +2 | N/A |
| Prostitution | 0 | 1 | +1 | N/A |

![](images/district_2D_categories.png)



\newpage
## 3D

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 62 | 314 | +252 | +406% |
| Liquor Law Violations | 49 | 244 | +195 | +398% |
| Motor Vehicle Theft | 2 | 8 | +6 | +300% |
| Theft | 208 | 552 | +344 | +165% |
| Robbery | 22 | 58 | +36 | +164% |
| Disorderly Conduct | 38 | 90 | +52 | +137% |
| Sex Abuse | 4 | 9 | +5 | +125% |
| Traffic Violations | 127 | 252 | +125 | +98% |
| Release Violations/Fugitive | 124 | 234 | +110 | +89% |
| Theft from Auto | 4 | 7 | +3 | +75% |
| Aggravated Assault | 20 | 33 | +13 | +65% |
| Other Crimes | 170 | 215 | +45 | +26% |
| Assault on a Police Officer | 50 | 62 | +12 | +24% |
| Burglary | 17 | 21 | +4 | +24% |
| Driving/Boating While Intoxicated | 83 | 100 | +17 | +20% |
| Offenses Against Family & Children | 33 | 37 | +4 | +12% |
| Damage to Property | 65 | 71 | +6 | +9% |
| Weapon Violations | 203 | 216 | +13 | +6% |
| Simple Assault | 573 | 583 | +10 | +2% |
| Gambling | 2 | 2 | +0 | 0% |
| Sex Offenses | 17 | 16 | -1 | -6% |
| Property Crimes | 66 | 60 | -6 | -9% |
| Assault with a Dangerous Weapon | 53 | 46 | -7 | -13% |
| Kidnapping | 2 | 1 | -1 | -50% |
| Fraud and Financial Crimes | 4 | 1 | -3 | -75% |
| Homicide | 8 | 2 | -6 | -75% |
| Arson | 2 | 0 | -2 | -100% |
| Prostitution | 0 | 4 | +4 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/district_3D_categories.png)



\newpage
## 4D

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Fraud and Financial Crimes | 1 | 9 | +8 | +800% |
| Theft from Auto | 1 | 5 | +4 | +400% |
| Liquor Law Violations | 7 | 26 | +19 | +271% |
| Motor Vehicle Theft | 2 | 6 | +4 | +200% |
| Theft | 51 | 149 | +98 | +192% |
| Disorderly Conduct | 4 | 10 | +6 | +150% |
| Burglary | 11 | 20 | +9 | +82% |
| Traffic Violations | 158 | 287 | +129 | +82% |
| Sex Offenses | 13 | 15 | +2 | +15% |
| Aggravated Assault | 14 | 16 | +2 | +14% |
| Driving/Boating While Intoxicated | 86 | 93 | +7 | +8% |
| Release Violations/Fugitive | 213 | 217 | +4 | +2% |
| Robbery | 24 | 24 | +0 | 0% |
| Simple Assault | 547 | 545 | -2 | 0% |
| Property Crimes | 48 | 43 | -5 | -10% |
| Assault with a Dangerous Weapon | 38 | 34 | -4 | -11% |
| Narcotics | 63 | 55 | -8 | -13% |
| Weapon Violations | 102 | 87 | -15 | -15% |
| Damage to Property | 70 | 52 | -18 | -26% |
| Other Crimes | 138 | 96 | -42 | -30% |
| Offenses Against Family & Children | 52 | 35 | -17 | -33% |
| Assault on a Police Officer | 25 | 13 | -12 | -48% |
| Homicide | 7 | 3 | -4 | -57% |
| Sex Abuse | 7 | 2 | -5 | -71% |
| Arson | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/district_4D_categories.png)



\newpage
## 5D

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 19 | 125 | +106 | +558% |
| Aggravated Assault | 17 | 47 | +30 | +176% |
| Traffic Violations | 151 | 358 | +207 | +137% |
| Narcotics | 81 | 187 | +106 | +131% |
| Theft from Auto | 3 | 6 | +3 | +100% |
| Fraud and Financial Crimes | 3 | 5 | +2 | +67% |
| Homicide | 6 | 10 | +4 | +67% |
| Theft | 174 | 260 | +86 | +49% |
| Motor Vehicle Theft | 7 | 10 | +3 | +43% |
| Robbery | 30 | 38 | +8 | +27% |
| Offenses Against Family & Children | 40 | 44 | +4 | +10% |
| Disorderly Conduct | 16 | 17 | +1 | +6% |
| Release Violations/Fugitive | 222 | 230 | +8 | +4% |
| Assault with a Dangerous Weapon | 59 | 59 | +0 | 0% |
| Driving/Boating While Intoxicated | 87 | 86 | -1 | -1% |
| Property Crimes | 71 | 67 | -4 | -6% |
| Weapon Violations | 189 | 157 | -32 | -17% |
| Simple Assault | 830 | 686 | -144 | -17% |
| Damage to Property | 106 | 84 | -22 | -21% |
| Burglary | 24 | 19 | -5 | -21% |
| Sex Offenses | 17 | 13 | -4 | -24% |
| Sex Abuse | 4 | 3 | -1 | -25% |
| Assault on a Police Officer | 56 | 40 | -16 | -29% |
| Other Crimes | 184 | 122 | -62 | -34% |
| Kidnapping | 3 | 1 | -2 | -67% |
| Vending Violations | 1 | 0 | -1 | -100% |
| Arson | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |

![](images/district_5D_categories.png)



\newpage
## 6D

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 93 | 1,113 | +1,020 | +1097% |
| Liquor Law Violations | 23 | 270 | +247 | +1074% |
| Fraud and Financial Crimes | 1 | 3 | +2 | +200% |
| Theft | 34 | 100 | +66 | +194% |
| Disorderly Conduct | 4 | 10 | +6 | +150% |
| Burglary | 12 | 26 | +14 | +117% |
| Narcotics | 87 | 177 | +90 | +103% |
| Motor Vehicle Theft | 2 | 4 | +2 | +100% |
| Aggravated Assault | 17 | 27 | +10 | +59% |
| Sex Offenses | 15 | 20 | +5 | +33% |
| Offenses Against Family & Children | 55 | 63 | +8 | +15% |
| Assault with a Dangerous Weapon | 66 | 75 | +9 | +14% |
| Assault on a Police Officer | 33 | 33 | +0 | 0% |
| Property Crimes | 120 | 114 | -6 | -5% |
| Homicide | 13 | 12 | -1 | -8% |
| Simple Assault | 892 | 823 | -69 | -8% |
| Release Violations/Fugitive | 246 | 224 | -22 | -9% |
| Robbery | 34 | 30 | -4 | -12% |
| Damage to Property | 114 | 99 | -15 | -13% |
| Weapon Violations | 367 | 264 | -103 | -28% |
| Other Crimes | 131 | 93 | -38 | -29% |
| Driving/Boating While Intoxicated | 68 | 41 | -27 | -40% |
| Sex Abuse | 8 | 4 | -4 | -50% |
| Kidnapping | 4 | 0 | -4 | -100% |
| Prostitution | 9 | 0 | -9 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Gambling | 0 | 3 | +3 | N/A |
| Theft from Auto | 0 | 3 | +3 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/district_6D_categories.png)



\newpage
## 7D

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 12 | 141 | +129 | +1075% |
| Burglary | 8 | 31 | +23 | +288% |
| Disorderly Conduct | 9 | 33 | +24 | +267% |
| Traffic Violations | 118 | 423 | +305 | +258% |
| Narcotics | 123 | 400 | +277 | +225% |
| Motor Vehicle Theft | 4 | 13 | +9 | +225% |
| Aggravated Assault | 27 | 70 | +43 | +159% |
| Theft from Auto | 1 | 2 | +1 | +100% |
| Theft | 44 | 78 | +34 | +77% |
| Other Crimes | 153 | 211 | +58 | +38% |
| Assault on a Police Officer | 73 | 94 | +21 | +29% |
| Property Crimes | 100 | 127 | +27 | +27% |
| Assault with a Dangerous Weapon | 80 | 96 | +16 | +20% |
| Weapon Violations | 310 | 359 | +49 | +16% |
| Arson | 1 | 1 | +0 | 0% |
| Release Violations/Fugitive | 262 | 250 | -12 | -5% |
| Sex Offenses | 21 | 19 | -2 | -10% |
| Simple Assault | 1,153 | 1,042 | -111 | -10% |
| Robbery | 27 | 24 | -3 | -11% |
| Driving/Boating While Intoxicated | 131 | 115 | -16 | -12% |
| Damage to Property | 125 | 107 | -18 | -14% |
| Offenses Against Family & Children | 96 | 82 | -14 | -15% |
| Kidnapping | 5 | 4 | -1 | -20% |
| Homicide | 13 | 10 | -3 | -23% |
| Sex Abuse | 13 | 9 | -4 | -31% |
| Fraud and Financial Crimes | 0 | 4 | +4 | N/A |
| Gambling | 0 | 2 | +2 | N/A |
| Prostitution | 0 | 10 | +10 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/district_7D_categories.png)



\newpage
## nan

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 5 | 37 | +32 | +640% |
| Traffic Violations | 13 | 82 | +69 | +531% |
| Damage to Property | 1 | 6 | +5 | +500% |
| Liquor Law Violations | 6 | 35 | +29 | +483% |
| Assault on a Police Officer | 2 | 8 | +6 | +300% |
| Release Violations/Fugitive | 4 | 16 | +12 | +300% |
| Theft | 4 | 13 | +9 | +225% |
| Driving/Boating While Intoxicated | 17 | 49 | +32 | +188% |
| Simple Assault | 18 | 39 | +21 | +117% |
| Offenses Against Family & Children | 1 | 2 | +1 | +100% |
| Property Crimes | 4 | 8 | +4 | +100% |
| Robbery | 2 | 4 | +2 | +100% |
| Weapon Violations | 13 | 26 | +13 | +100% |
| Assault with a Dangerous Weapon | 3 | 4 | +1 | +33% |
| Burglary | 1 | 0 | -1 | -100% |
| Other Crimes | 1 | 0 | -1 | -100% |
| Aggravated Assault | 0 | 1 | +1 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 8 | +8 | N/A |
| Fraud and Financial Crimes | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 3 | +3 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Sex Offenses | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/district_nan_categories.png)



\newpage
# Appendix 3: Data by ANC

\newpage
## ANC 1A

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 10 | 37 | +27 | +270% |
| Theft | 106 | 363 | +257 | +242% |
| Narcotics | 16 | 44 | +28 | +175% |
| Aggravated Assault | 2 | 5 | +3 | +150% |
| Traffic Violations | 28 | 66 | +38 | +136% |
| Disorderly Conduct | 2 | 4 | +2 | +100% |
| Offenses Against Family & Children | 7 | 12 | +5 | +71% |
| Robbery | 7 | 12 | +5 | +71% |
| Property Crimes | 9 | 14 | +5 | +56% |
| Assault on a Police Officer | 13 | 19 | +6 | +46% |
| Damage to Property | 12 | 15 | +3 | +25% |
| Release Violations/Fugitive | 38 | 40 | +2 | +5% |
| Simple Assault | 122 | 127 | +5 | +4% |
| Sex Abuse | 1 | 1 | +0 | 0% |
| Weapon Violations | 36 | 36 | +0 | 0% |
| Driving/Boating While Intoxicated | 20 | 13 | -7 | -35% |
| Other Crimes | 62 | 40 | -22 | -35% |
| Sex Offenses | 5 | 3 | -2 | -40% |
| Assault with a Dangerous Weapon | 17 | 9 | -8 | -47% |
| Kidnapping | 2 | 1 | -1 | -50% |
| Fraud and Financial Crimes | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Burglary | 0 | 5 | +5 | N/A |
| Gambling | 0 | 1 | +1 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 2 | +2 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 2 | +2 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_1A_categories.png)

\newpage
## ANC 1B

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 26 | 155 | +129 | +496% |
| Liquor Law Violations | 17 | 89 | +72 | +424% |
| Motor Vehicle Theft | 1 | 4 | +3 | +300% |
| Sex Abuse | 1 | 3 | +2 | +200% |
| Theft | 31 | 80 | +49 | +158% |
| Release Violations/Fugitive | 41 | 105 | +64 | +156% |
| Robbery | 9 | 23 | +14 | +156% |
| Disorderly Conduct | 24 | 58 | +34 | +142% |
| Other Crimes | 36 | 70 | +34 | +94% |
| Aggravated Assault | 6 | 11 | +5 | +83% |
| Theft from Auto | 3 | 5 | +2 | +67% |
| Traffic Violations | 47 | 74 | +27 | +57% |
| Damage to Property | 14 | 22 | +8 | +57% |
| Weapon Violations | 78 | 120 | +42 | +54% |
| Driving/Boating While Intoxicated | 22 | 32 | +10 | +45% |
| Simple Assault | 118 | 160 | +42 | +36% |
| Assault on a Police Officer | 19 | 25 | +6 | +32% |
| Property Crimes | 12 | 13 | +1 | +8% |
| Offenses Against Family & Children | 9 | 8 | -1 | -11% |
| Burglary | 8 | 7 | -1 | -12% |
| Sex Offenses | 3 | 2 | -1 | -33% |
| Assault with a Dangerous Weapon | 21 | 13 | -8 | -38% |
| Arson | 1 | 0 | -1 | -100% |
| Fraud and Financial Crimes | 3 | 0 | -3 | -100% |
| Homicide | 1 | 0 | -1 | -100% |
| Gambling | 0 | 1 | +1 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_1B_categories.png)

\newpage
## ANC 1C

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 1 | 33 | +32 | +3200% |
| Traffic Violations | 4 | 21 | +17 | +425% |
| Narcotics | 4 | 18 | +14 | +350% |
| Disorderly Conduct | 1 | 4 | +3 | +300% |
| Aggravated Assault | 3 | 6 | +3 | +100% |
| Assault with a Dangerous Weapon | 2 | 4 | +2 | +100% |
| Burglary | 2 | 4 | +2 | +100% |
| Sex Abuse | 1 | 2 | +1 | +100% |
| Sex Offenses | 3 | 5 | +2 | +67% |
| Theft | 20 | 31 | +11 | +55% |
| Release Violations/Fugitive | 13 | 20 | +7 | +54% |
| Other Crimes | 21 | 23 | +2 | +10% |
| Driving/Boating While Intoxicated | 7 | 6 | -1 | -14% |
| Simple Assault | 76 | 59 | -17 | -22% |
| Weapon Violations | 7 | 5 | -2 | -29% |
| Robbery | 3 | 2 | -1 | -33% |
| Assault on a Police Officer | 5 | 3 | -2 | -40% |
| Offenses Against Family & Children | 5 | 3 | -2 | -40% |
| Damage to Property | 15 | 7 | -8 | -53% |
| Gambling | 2 | 0 | -2 | -100% |
| Property Crimes | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_1C_categories.png)

\newpage
## ANC 1D

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 1 | 29 | +28 | +2800% |
| Robbery | 1 | 6 | +5 | +500% |
| Liquor Law Violations | 8 | 46 | +38 | +475% |
| Disorderly Conduct | 3 | 10 | +7 | +233% |
| Burglary | 2 | 6 | +4 | +200% |
| Release Violations/Fugitive | 16 | 38 | +22 | +138% |
| Traffic Violations | 8 | 18 | +10 | +125% |
| Offenses Against Family & Children | 3 | 4 | +1 | +33% |
| Assault with a Dangerous Weapon | 8 | 10 | +2 | +25% |
| Driving/Boating While Intoxicated | 4 | 5 | +1 | +25% |
| Property Crimes | 4 | 5 | +1 | +25% |
| Other Crimes | 21 | 26 | +5 | +24% |
| Simple Assault | 72 | 78 | +6 | +8% |
| Aggravated Assault | 4 | 4 | +0 | 0% |
| Weapon Violations | 6 | 6 | +0 | 0% |
| Damage to Property | 7 | 6 | -1 | -14% |
| Assault on a Police Officer | 2 | 1 | -1 | -50% |
| Homicide | 2 | 1 | -1 | -50% |
| Theft | 15 | 7 | -8 | -53% |
| Sex Offenses | 5 | 2 | -3 | -60% |
| Sex Abuse | 1 | 0 | -1 | -100% |
| Theft from Auto | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_1D_categories.png)

\newpage
## ANC 1E

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Disorderly Conduct | 1 | 4 | +3 | +300% |
| Narcotics | 6 | 19 | +13 | +217% |
| Theft | 13 | 29 | +16 | +123% |
| Traffic Violations | 19 | 41 | +22 | +116% |
| Damage to Property | 7 | 12 | +5 | +71% |
| Release Violations/Fugitive | 20 | 32 | +12 | +60% |
| Robbery | 3 | 4 | +1 | +33% |
| Driving/Boating While Intoxicated | 14 | 17 | +3 | +21% |
| Simple Assault | 66 | 80 | +14 | +21% |
| Liquor Law Violations | 3 | 3 | +0 | 0% |
| Weapon Violations | 23 | 22 | -1 | -4% |
| Property Crimes | 9 | 7 | -2 | -22% |
| Assault on a Police Officer | 4 | 3 | -1 | -25% |
| Assault with a Dangerous Weapon | 6 | 4 | -2 | -33% |
| Other Crimes | 30 | 17 | -13 | -43% |
| Sex Offenses | 4 | 2 | -2 | -50% |
| Burglary | 5 | 2 | -3 | -60% |
| Offenses Against Family & Children | 8 | 1 | -7 | -88% |
| Aggravated Assault | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 2 | +2 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 2 | +2 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_1E_categories.png)

\newpage
## ANC 2A

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Offenses Against Family & Children | 1 | 7 | +6 | +600% |
| Other Crimes | 9 | 53 | +44 | +489% |
| Property Crimes | 1 | 4 | +3 | +300% |
| Assault on a Police Officer | 3 | 9 | +6 | +200% |
| Theft | 9 | 23 | +14 | +156% |
| Burglary | 1 | 2 | +1 | +100% |
| Driving/Boating While Intoxicated | 9 | 10 | +1 | +11% |
| Traffic Violations | 14 | 15 | +1 | +7% |
| Fraud and Financial Crimes | 1 | 1 | +0 | 0% |
| Simple Assault | 58 | 48 | -10 | -17% |
| Assault with a Dangerous Weapon | 5 | 4 | -1 | -20% |
| Release Violations/Fugitive | 25 | 16 | -9 | -36% |
| Damage to Property | 8 | 3 | -5 | -62% |
| Weapon Violations | 18 | 6 | -12 | -67% |
| Sex Offenses | 6 | 1 | -5 | -83% |
| Aggravated Assault | 2 | 0 | -2 | -100% |
| Motor Vehicle Theft | 2 | 0 | -2 | -100% |
| Narcotics | 3 | 0 | -3 | -100% |
| Sex Abuse | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 1 | +1 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Robbery | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_2A_categories.png)

\newpage
## ANC 2B

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 2 | 6 | +4 | +200% |
| Sex Offenses | 1 | 3 | +2 | +200% |
| Offenses Against Family & Children | 1 | 2 | +1 | +100% |
| Theft | 28 | 39 | +11 | +39% |
| Damage to Property | 11 | 14 | +3 | +27% |
| Assault on a Police Officer | 5 | 6 | +1 | +20% |
| Traffic Violations | 38 | 45 | +7 | +18% |
| Burglary | 1 | 1 | +0 | 0% |
| Other Crimes | 13 | 12 | -1 | -8% |
| Driving/Boating While Intoxicated | 14 | 12 | -2 | -14% |
| Simple Assault | 82 | 63 | -19 | -23% |
| Property Crimes | 9 | 6 | -3 | -33% |
| Assault with a Dangerous Weapon | 7 | 4 | -3 | -43% |
| Disorderly Conduct | 9 | 5 | -4 | -44% |
| Release Violations/Fugitive | 13 | 5 | -8 | -62% |
| Weapon Violations | 53 | 20 | -33 | -62% |
| Aggravated Assault | 2 | 0 | -2 | -100% |
| Fraud and Financial Crimes | 2 | 0 | -2 | -100% |
| Motor Vehicle Theft | 1 | 0 | -1 | -100% |
| Narcotics | 3 | 0 | -3 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Robbery | 0 | 2 | +2 | N/A |
| Sex Abuse | 0 | 2 | +2 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_2B_categories.png)

\newpage
## ANC 2C

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Aggravated Assault | 3 | 6 | +3 | +100% |
| Theft | 76 | 130 | +54 | +71% |
| Traffic Violations | 48 | 76 | +28 | +58% |
| Driving/Boating While Intoxicated | 22 | 30 | +8 | +36% |
| Burglary | 3 | 4 | +1 | +33% |
| Assault with a Dangerous Weapon | 7 | 9 | +2 | +29% |
| Fraud and Financial Crimes | 4 | 4 | +0 | 0% |
| Homicide | 1 | 1 | +0 | 0% |
| Assault on a Police Officer | 15 | 14 | -1 | -7% |
| Simple Assault | 144 | 133 | -11 | -8% |
| Robbery | 6 | 5 | -1 | -17% |
| Narcotics | 51 | 39 | -12 | -24% |
| Weapon Violations | 72 | 51 | -21 | -29% |
| Damage to Property | 20 | 14 | -6 | -30% |
| Liquor Law Violations | 34 | 23 | -11 | -32% |
| Release Violations/Fugitive | 100 | 62 | -38 | -38% |
| Motor Vehicle Theft | 2 | 1 | -1 | -50% |
| Offenses Against Family & Children | 6 | 3 | -3 | -50% |
| Other Crimes | 73 | 35 | -38 | -52% |
| Disorderly Conduct | 14 | 6 | -8 | -57% |
| Property Crimes | 17 | 6 | -11 | -65% |
| Sex Abuse | 3 | 1 | -2 | -67% |
| Sex Offenses | 8 | 1 | -7 | -88% |
| Gambling | 3 | 0 | -3 | -100% |
| Vending Violations | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 3 | +3 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |

![](images/anc_2C_categories.png)

\newpage
## ANC 2D

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 3 | 4 | +1 | +33% |
| Simple Assault | 2 | 2 | +0 | 0% |
| Weapon Violations | 5 | 3 | -2 | -40% |
| Assault with a Dangerous Weapon | 1 | 0 | -1 | -100% |
| Damage to Property | 2 | 0 | -2 | -100% |
| Driving/Boating While Intoxicated | 3 | 0 | -3 | -100% |
| Other Crimes | 4 | 0 | -4 | -100% |
| Robbery | 2 | 0 | -2 | -100% |
| Sex Abuse | 1 | 0 | -1 | -100% |
| Aggravated Assault | 0 | 0 | +0 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Assault on a Police Officer | 0 | 0 | +0 | N/A |
| Burglary | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Narcotics | 0 | 0 | +0 | N/A |
| Offenses Against Family & Children | 0 | 1 | +1 | N/A |
| Property Crimes | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Release Violations/Fugitive | 0 | 0 | +0 | N/A |
| Sex Offenses | 0 | 0 | +0 | N/A |
| Theft | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_2D_categories.png)

\newpage
## ANC 2E

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 3 | 20 | +17 | +567% |
| Assault with a Dangerous Weapon | 1 | 3 | +2 | +200% |
| Release Violations/Fugitive | 7 | 18 | +11 | +157% |
| Theft | 13 | 29 | +16 | +123% |
| Liquor Law Violations | 1 | 2 | +1 | +100% |
| Driving/Boating While Intoxicated | 5 | 8 | +3 | +60% |
| Weapon Violations | 2 | 3 | +1 | +50% |
| Damage to Property | 6 | 8 | +2 | +33% |
| Property Crimes | 4 | 5 | +1 | +25% |
| Simple Assault | 24 | 29 | +5 | +21% |
| Other Crimes | 16 | 18 | +2 | +12% |
| Sex Offenses | 1 | 1 | +0 | 0% |
| Robbery | 2 | 1 | -1 | -50% |
| Assault on a Police Officer | 5 | 2 | -3 | -60% |
| Burglary | 3 | 0 | -3 | -100% |
| Fraud and Financial Crimes | 3 | 0 | -3 | -100% |
| Offenses Against Family & Children | 2 | 0 | -2 | -100% |
| Aggravated Assault | 0 | 0 | +0 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Narcotics | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_2E_categories.png)

\newpage
## ANC 2F

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 2 | 13 | +11 | +550% |
| Disorderly Conduct | 1 | 5 | +4 | +400% |
| Assault on a Police Officer | 2 | 9 | +7 | +350% |
| Driving/Boating While Intoxicated | 8 | 21 | +13 | +162% |
| Offenses Against Family & Children | 2 | 5 | +3 | +150% |
| Robbery | 2 | 5 | +3 | +150% |
| Assault with a Dangerous Weapon | 3 | 7 | +4 | +133% |
| Release Violations/Fugitive | 12 | 24 | +12 | +100% |
| Sex Offenses | 1 | 2 | +1 | +100% |
| Weapon Violations | 13 | 20 | +7 | +54% |
| Theft | 37 | 46 | +9 | +24% |
| Traffic Violations | 29 | 36 | +7 | +24% |
| Simple Assault | 63 | 68 | +5 | +8% |
| Other Crimes | 19 | 18 | -1 | -5% |
| Damage to Property | 5 | 3 | -2 | -40% |
| Property Crimes | 9 | 2 | -7 | -78% |
| Burglary | 1 | 0 | -1 | -100% |
| Fraud and Financial Crimes | 1 | 0 | -1 | -100% |
| Homicide | 2 | 0 | -2 | -100% |
| Kidnapping | 1 | 0 | -1 | -100% |
| Theft from Auto | 1 | 0 | -1 | -100% |
| Aggravated Assault | 0 | 2 | +2 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 16 | +16 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 4 | +4 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_2F_categories.png)

\newpage
## ANC 2G

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 7 | 42 | +35 | +500% |
| Liquor Law Violations | 7 | 35 | +28 | +400% |
| Damage to Property | 4 | 11 | +7 | +175% |
| Theft | 14 | 32 | +18 | +129% |
| Aggravated Assault | 2 | 4 | +2 | +100% |
| Disorderly Conduct | 4 | 6 | +2 | +50% |
| Traffic Violations | 17 | 25 | +8 | +47% |
| Assault with a Dangerous Weapon | 4 | 5 | +1 | +25% |
| Release Violations/Fugitive | 16 | 20 | +4 | +25% |
| Driving/Boating While Intoxicated | 15 | 17 | +2 | +13% |
| Other Crimes | 13 | 14 | +1 | +8% |
| Homicide | 1 | 1 | +0 | 0% |
| Weapon Violations | 30 | 27 | -3 | -10% |
| Property Crimes | 17 | 14 | -3 | -18% |
| Simple Assault | 83 | 67 | -16 | -19% |
| Offenses Against Family & Children | 5 | 4 | -1 | -20% |
| Assault on a Police Officer | 8 | 4 | -4 | -50% |
| Burglary | 2 | 1 | -1 | -50% |
| Arson | 1 | 0 | -1 | -100% |
| Motor Vehicle Theft | 1 | 0 | -1 | -100% |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Robbery | 0 | 11 | +11 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Sex Offenses | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_2G_categories.png)

\newpage
## ANC 3/4G

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Release Violations/Fugitive | 3 | 6 | +3 | +100% |
| Driving/Boating While Intoxicated | 2 | 3 | +1 | +50% |
| Assault with a Dangerous Weapon | 1 | 1 | +0 | 0% |
| Other Crimes | 3 | 2 | -1 | -33% |
| Simple Assault | 12 | 7 | -5 | -42% |
| Traffic Violations | 5 | 1 | -4 | -80% |
| Burglary | 2 | 0 | -2 | -100% |
| Damage to Property | 1 | 0 | -1 | -100% |
| Weapon Violations | 1 | 0 | -1 | -100% |
| Aggravated Assault | 0 | 0 | +0 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Assault on a Police Officer | 0 | 1 | +1 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Narcotics | 0 | 0 | +0 | N/A |
| Offenses Against Family & Children | 0 | 2 | +2 | N/A |
| Property Crimes | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Robbery | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Sex Offenses | 0 | 0 | +0 | N/A |
| Theft | 0 | 3 | +3 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_3-4G_categories.png)

\newpage
## ANC 3A

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 3 | 15 | +12 | +400% |
| Assault with a Dangerous Weapon | 2 | 6 | +4 | +200% |
| Theft | 12 | 28 | +16 | +133% |
| Disorderly Conduct | 1 | 2 | +1 | +100% |
| Offenses Against Family & Children | 2 | 4 | +2 | +100% |
| Sex Offenses | 1 | 2 | +1 | +100% |
| Damage to Property | 4 | 6 | +2 | +50% |
| Simple Assault | 26 | 37 | +11 | +42% |
| Aggravated Assault | 2 | 2 | +0 | 0% |
| Burglary | 1 | 1 | +0 | 0% |
| Driving/Boating While Intoxicated | 4 | 4 | +0 | 0% |
| Motor Vehicle Theft | 1 | 1 | +0 | 0% |
| Weapon Violations | 6 | 6 | +0 | 0% |
| Other Crimes | 8 | 7 | -1 | -12% |
| Release Violations/Fugitive | 11 | 9 | -2 | -18% |
| Robbery | 5 | 4 | -1 | -20% |
| Property Crimes | 3 | 1 | -2 | -67% |
| Arson | 1 | 0 | -1 | -100% |
| Assault on a Police Officer | 1 | 0 | -1 | -100% |
| Narcotics | 1 | 0 | -1 | -100% |
| Vending Violations | 2 | 0 | -2 | -100% |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 1 | +1 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |

![](images/anc_3A_categories.png)

\newpage
## ANC 3B

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Theft | 2 | 4 | +2 | +100% |
| Driving/Boating While Intoxicated | 1 | 1 | +0 | 0% |
| Other Crimes | 1 | 1 | +0 | 0% |
| Simple Assault | 16 | 15 | -1 | -6% |
| Assault with a Dangerous Weapon | 2 | 1 | -1 | -50% |
| Damage to Property | 3 | 0 | -3 | -100% |
| Robbery | 2 | 0 | -2 | -100% |
| Theft from Auto | 2 | 0 | -2 | -100% |
| Aggravated Assault | 0 | 0 | +0 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Assault on a Police Officer | 0 | 1 | +1 | N/A |
| Burglary | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Narcotics | 0 | 0 | +0 | N/A |
| Offenses Against Family & Children | 0 | 0 | +0 | N/A |
| Property Crimes | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Release Violations/Fugitive | 0 | 2 | +2 | N/A |
| Sex Abuse | 0 | 1 | +1 | N/A |
| Sex Offenses | 0 | 1 | +1 | N/A |
| Traffic Violations | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |
| Weapon Violations | 0 | 0 | +0 | N/A |

![](images/anc_3B_categories.png)

\newpage
## ANC 3C

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Assault on a Police Officer | 1 | 3 | +2 | +200% |
| Traffic Violations | 5 | 10 | +5 | +100% |
| Sex Offenses | 1 | 1 | +0 | 0% |
| Weapon Violations | 2 | 2 | +0 | 0% |
| Release Violations/Fugitive | 12 | 10 | -2 | -17% |
| Assault with a Dangerous Weapon | 4 | 3 | -1 | -25% |
| Damage to Property | 5 | 3 | -2 | -40% |
| Theft | 48 | 27 | -21 | -44% |
| Other Crimes | 11 | 6 | -5 | -45% |
| Driving/Boating While Intoxicated | 6 | 3 | -3 | -50% |
| Robbery | 2 | 1 | -1 | -50% |
| Simple Assault | 52 | 22 | -30 | -58% |
| Offenses Against Family & Children | 6 | 2 | -4 | -67% |
| Burglary | 4 | 0 | -4 | -100% |
| Property Crimes | 1 | 0 | -1 | -100% |
| Theft from Auto | 1 | 0 | -1 | -100% |
| Aggravated Assault | 0 | 1 | +1 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Narcotics | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_3C_categories.png)

\newpage
## ANC 3D

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Other Crimes | 2 | 3 | +1 | +50% |
| Traffic Violations | 2 | 3 | +1 | +50% |
| Driving/Boating While Intoxicated | 2 | 2 | +0 | 0% |
| Release Violations/Fugitive | 3 | 3 | +0 | 0% |
| Simple Assault | 10 | 7 | -3 | -30% |
| Assault with a Dangerous Weapon | 1 | 0 | -1 | -100% |
| Damage to Property | 1 | 0 | -1 | -100% |
| Offenses Against Family & Children | 2 | 0 | -2 | -100% |
| Sex Abuse | 1 | 0 | -1 | -100% |
| Theft | 2 | 0 | -2 | -100% |
| Aggravated Assault | 0 | 1 | +1 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Assault on a Police Officer | 0 | 1 | +1 | N/A |
| Burglary | 0 | 1 | +1 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Narcotics | 0 | 0 | +0 | N/A |
| Property Crimes | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Robbery | 0 | 0 | +0 | N/A |
| Sex Offenses | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |
| Weapon Violations | 0 | 0 | +0 | N/A |

![](images/anc_3D_categories.png)

\newpage
## ANC 3E

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Driving/Boating While Intoxicated | 1 | 6 | +5 | +500% |
| Weapon Violations | 2 | 3 | +1 | +50% |
| Damage to Property | 4 | 5 | +1 | +25% |
| Theft | 21 | 25 | +4 | +19% |
| Assault with a Dangerous Weapon | 1 | 1 | +0 | 0% |
| Sex Offenses | 1 | 1 | +0 | 0% |
| Simple Assault | 11 | 10 | -1 | -9% |
| Other Crimes | 6 | 3 | -3 | -50% |
| Release Violations/Fugitive | 6 | 2 | -4 | -67% |
| Aggravated Assault | 0 | 0 | +0 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Assault on a Police Officer | 0 | 2 | +2 | N/A |
| Burglary | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 1 | +1 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Narcotics | 0 | 3 | +3 | N/A |
| Offenses Against Family & Children | 0 | 0 | +0 | N/A |
| Property Crimes | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Robbery | 0 | 1 | +1 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |
| Traffic Violations | 0 | 3 | +3 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_3E_categories.png)

\newpage
## ANC 3F

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Theft | 7 | 20 | +13 | +186% |
| Other Crimes | 5 | 12 | +7 | +140% |
| Release Violations/Fugitive | 5 | 12 | +7 | +140% |
| Damage to Property | 3 | 5 | +2 | +67% |
| Assault on a Police Officer | 2 | 3 | +1 | +50% |
| Driving/Boating While Intoxicated | 2 | 3 | +1 | +50% |
| Offenses Against Family & Children | 3 | 4 | +1 | +33% |
| Simple Assault | 34 | 35 | +1 | +3% |
| Property Crimes | 1 | 1 | +0 | 0% |
| Sex Offenses | 2 | 2 | +0 | 0% |
| Narcotics | 2 | 1 | -1 | -50% |
| Weapon Violations | 2 | 1 | -1 | -50% |
| Traffic Violations | 7 | 3 | -4 | -57% |
| Assault with a Dangerous Weapon | 5 | 1 | -4 | -80% |
| Liquor Law Violations | 1 | 0 | -1 | -100% |
| Motor Vehicle Theft | 1 | 0 | -1 | -100% |
| Aggravated Assault | 0 | 1 | +1 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Burglary | 0 | 1 | +1 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Robbery | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_3F_categories.png)

\newpage
## ANC 4A

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 1 | 7 | +6 | +600% |
| Theft | 6 | 36 | +30 | +500% |
| Weapon Violations | 1 | 5 | +4 | +400% |
| Traffic Violations | 10 | 23 | +13 | +130% |
| Burglary | 1 | 2 | +1 | +100% |
| Disorderly Conduct | 1 | 2 | +1 | +100% |
| Motor Vehicle Theft | 1 | 2 | +1 | +100% |
| Offenses Against Family & Children | 2 | 4 | +2 | +100% |
| Robbery | 1 | 2 | +1 | +100% |
| Driving/Boating While Intoxicated | 7 | 13 | +6 | +86% |
| Simple Assault | 58 | 69 | +11 | +19% |
| Release Violations/Fugitive | 14 | 15 | +1 | +7% |
| Damage to Property | 5 | 5 | +0 | 0% |
| Sex Offenses | 1 | 1 | +0 | 0% |
| Other Crimes | 8 | 7 | -1 | -12% |
| Property Crimes | 3 | 2 | -1 | -33% |
| Aggravated Assault | 2 | 1 | -1 | -50% |
| Assault on a Police Officer | 1 | 0 | -1 | -100% |
| Homicide | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Assault with a Dangerous Weapon | 0 | 3 | +3 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 4 | +4 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_4A_categories.png)

\newpage
## ANC 4B

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 1 | 6 | +5 | +500% |
| Fraud and Financial Crimes | 1 | 4 | +3 | +300% |
| Theft | 15 | 30 | +15 | +100% |
| Narcotics | 4 | 7 | +3 | +75% |
| Traffic Violations | 26 | 45 | +19 | +73% |
| Release Violations/Fugitive | 28 | 38 | +10 | +36% |
| Driving/Boating While Intoxicated | 18 | 19 | +1 | +6% |
| Other Crimes | 20 | 21 | +1 | +5% |
| Disorderly Conduct | 1 | 1 | +0 | 0% |
| Property Crimes | 7 | 7 | +0 | 0% |
| Sex Abuse | 1 | 1 | +0 | 0% |
| Sex Offenses | 2 | 2 | +0 | 0% |
| Simple Assault | 92 | 91 | -1 | -1% |
| Damage to Property | 14 | 13 | -1 | -7% |
| Weapon Violations | 14 | 10 | -4 | -29% |
| Assault on a Police Officer | 8 | 4 | -4 | -50% |
| Burglary | 2 | 1 | -1 | -50% |
| Offenses Against Family & Children | 14 | 7 | -7 | -50% |
| Assault with a Dangerous Weapon | 7 | 3 | -4 | -57% |
| Robbery | 5 | 2 | -3 | -60% |
| Aggravated Assault | 4 | 1 | -3 | -75% |
| Arson | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 1 | +1 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_4B_categories.png)

\newpage
## ANC 4C

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Robbery | 1 | 9 | +8 | +800% |
| Theft | 10 | 31 | +21 | +210% |
| Traffic Violations | 33 | 67 | +34 | +103% |
| Burglary | 2 | 4 | +2 | +100% |
| Liquor Law Violations | 1 | 2 | +1 | +100% |
| Release Violations/Fugitive | 53 | 56 | +3 | +6% |
| Assault on a Police Officer | 2 | 2 | +0 | 0% |
| Assault with a Dangerous Weapon | 5 | 5 | +0 | 0% |
| Offenses Against Family & Children | 5 | 5 | +0 | 0% |
| Property Crimes | 7 | 7 | +0 | 0% |
| Sex Offenses | 2 | 2 | +0 | 0% |
| Simple Assault | 80 | 80 | +0 | 0% |
| Driving/Boating While Intoxicated | 16 | 15 | -1 | -6% |
| Other Crimes | 44 | 35 | -9 | -20% |
| Damage to Property | 18 | 13 | -5 | -28% |
| Narcotics | 25 | 10 | -15 | -60% |
| Aggravated Assault | 3 | 1 | -2 | -67% |
| Weapon Violations | 36 | 11 | -25 | -69% |
| Homicide | 2 | 0 | -2 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 3 | +3 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 2 | +2 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_4C_categories.png)

\newpage
## ANC 4D

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Theft | 2 | 13 | +11 | +550% |
| Assault on a Police Officer | 1 | 4 | +3 | +300% |
| Liquor Law Violations | 1 | 4 | +3 | +300% |
| Sex Offenses | 1 | 4 | +3 | +300% |
| Aggravated Assault | 2 | 6 | +4 | +200% |
| Driving/Boating While Intoxicated | 12 | 14 | +2 | +17% |
| Property Crimes | 6 | 7 | +1 | +17% |
| Weapon Violations | 14 | 16 | +2 | +14% |
| Traffic Violations | 32 | 36 | +4 | +12% |
| Release Violations/Fugitive | 19 | 21 | +2 | +11% |
| Simple Assault | 80 | 86 | +6 | +8% |
| Assault with a Dangerous Weapon | 5 | 5 | +0 | 0% |
| Damage to Property | 7 | 5 | -2 | -29% |
| Narcotics | 11 | 7 | -4 | -36% |
| Offenses Against Family & Children | 13 | 7 | -6 | -46% |
| Burglary | 2 | 1 | -1 | -50% |
| Other Crimes | 11 | 5 | -6 | -55% |
| Robbery | 4 | 1 | -3 | -75% |
| Homicide | 1 | 0 | -1 | -100% |
| Sex Abuse | 2 | 0 | -2 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 2 | +2 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_4D_categories.png)

\newpage
## ANC 4E

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 16 | 49 | +33 | +206% |
| Theft | 2 | 6 | +4 | +200% |
| Aggravated Assault | 1 | 2 | +1 | +100% |
| Assault with a Dangerous Weapon | 4 | 7 | +3 | +75% |
| Property Crimes | 6 | 10 | +4 | +67% |
| Driving/Boating While Intoxicated | 10 | 14 | +4 | +40% |
| Other Crimes | 5 | 6 | +1 | +20% |
| Liquor Law Violations | 2 | 2 | +0 | 0% |
| Motor Vehicle Theft | 1 | 1 | +0 | 0% |
| Simple Assault | 47 | 44 | -3 | -6% |
| Weapon Violations | 10 | 8 | -2 | -20% |
| Release Violations/Fugitive | 7 | 5 | -2 | -29% |
| Damage to Property | 5 | 3 | -2 | -40% |
| Robbery | 2 | 1 | -1 | -50% |
| Narcotics | 7 | 3 | -4 | -57% |
| Assault on a Police Officer | 2 | 0 | -2 | -100% |
| Sex Abuse | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Burglary | 0 | 3 | +3 | N/A |
| Disorderly Conduct | 0 | 2 | +2 | N/A |
| Fraud and Financial Crimes | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Offenses Against Family & Children | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Offenses | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_4E_categories.png)

\newpage
## ANC 5A

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Weapon Violations | 4 | 13 | +9 | +225% |
| Traffic Violations | 12 | 29 | +17 | +142% |
| Aggravated Assault | 1 | 2 | +1 | +100% |
| Theft | 3 | 5 | +2 | +67% |
| Offenses Against Family & Children | 4 | 5 | +1 | +25% |
| Narcotics | 2 | 2 | +0 | 0% |
| Simple Assault | 70 | 56 | -14 | -20% |
| Release Violations/Fugitive | 13 | 10 | -3 | -23% |
| Other Crimes | 11 | 7 | -4 | -36% |
| Driving/Boating While Intoxicated | 11 | 6 | -5 | -45% |
| Assault on a Police Officer | 2 | 1 | -1 | -50% |
| Assault with a Dangerous Weapon | 2 | 1 | -1 | -50% |
| Burglary | 2 | 1 | -1 | -50% |
| Property Crimes | 8 | 3 | -5 | -62% |
| Sex Offenses | 3 | 1 | -2 | -67% |
| Damage to Property | 6 | 1 | -5 | -83% |
| Robbery | 1 | 0 | -1 | -100% |
| Sex Abuse | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 2 | +2 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 1 | +1 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_5A_categories.png)

\newpage
## ANC 5B

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Theft | 5 | 12 | +7 | +140% |
| Property Crimes | 1 | 2 | +1 | +100% |
| Damage to Property | 6 | 9 | +3 | +50% |
| Liquor Law Violations | 2 | 3 | +1 | +50% |
| Robbery | 4 | 6 | +2 | +50% |
| Release Violations/Fugitive | 43 | 45 | +2 | +5% |
| Simple Assault | 44 | 45 | +1 | +2% |
| Burglary | 2 | 2 | +0 | 0% |
| Offenses Against Family & Children | 4 | 4 | +0 | 0% |
| Traffic Violations | 15 | 14 | -1 | -7% |
| Driving/Boating While Intoxicated | 10 | 9 | -1 | -10% |
| Other Crimes | 6 | 4 | -2 | -33% |
| Narcotics | 6 | 3 | -3 | -50% |
| Sex Offenses | 2 | 1 | -1 | -50% |
| Weapon Violations | 14 | 4 | -10 | -71% |
| Assault on a Police Officer | 5 | 1 | -4 | -80% |
| Assault with a Dangerous Weapon | 8 | 1 | -7 | -88% |
| Disorderly Conduct | 2 | 0 | -2 | -100% |
| Sex Abuse | 2 | 0 | -2 | -100% |
| Aggravated Assault | 0 | 2 | +2 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_5B_categories.png)

\newpage
## ANC 5C

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Offenses Against Family & Children | 3 | 9 | +6 | +200% |
| Narcotics | 10 | 25 | +15 | +150% |
| Traffic Violations | 58 | 135 | +77 | +133% |
| Aggravated Assault | 4 | 9 | +5 | +125% |
| Liquor Law Violations | 4 | 9 | +5 | +125% |
| Fraud and Financial Crimes | 2 | 3 | +1 | +50% |
| Sex Offenses | 5 | 7 | +2 | +40% |
| Property Crimes | 13 | 16 | +3 | +23% |
| Driving/Boating While Intoxicated | 27 | 32 | +5 | +19% |
| Homicide | 1 | 1 | +0 | 0% |
| Motor Vehicle Theft | 1 | 1 | +0 | 0% |
| Damage to Property | 25 | 23 | -2 | -8% |
| Robbery | 8 | 7 | -1 | -12% |
| Assault on a Police Officer | 13 | 11 | -2 | -15% |
| Assault with a Dangerous Weapon | 13 | 11 | -2 | -15% |
| Release Violations/Fugitive | 43 | 35 | -8 | -19% |
| Simple Assault | 195 | 148 | -47 | -24% |
| Weapon Violations | 42 | 25 | -17 | -40% |
| Theft | 78 | 46 | -32 | -41% |
| Other Crimes | 88 | 38 | -50 | -57% |
| Burglary | 7 | 3 | -4 | -57% |
| Disorderly Conduct | 10 | 0 | -10 | -100% |
| Sex Abuse | 2 | 0 | -2 | -100% |
| Vending Violations | 1 | 0 | -1 | -100% |
| Arson | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |

![](images/anc_5C_categories.png)

\newpage
## ANC 5D

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 5 | 88 | +83 | +1660% |
| Narcotics | 29 | 98 | +69 | +238% |
| Theft | 50 | 146 | +96 | +192% |
| Traffic Violations | 59 | 155 | +96 | +163% |
| Disorderly Conduct | 5 | 11 | +6 | +120% |
| Aggravated Assault | 11 | 22 | +11 | +100% |
| Homicide | 2 | 4 | +2 | +100% |
| Theft from Auto | 2 | 4 | +2 | +100% |
| Assault with a Dangerous Weapon | 21 | 26 | +5 | +24% |
| Driving/Boating While Intoxicated | 23 | 23 | +0 | 0% |
| Robbery | 11 | 11 | +0 | 0% |
| Other Crimes | 42 | 41 | -1 | -2% |
| Release Violations/Fugitive | 85 | 82 | -3 | -4% |
| Simple Assault | 311 | 279 | -32 | -10% |
| Weapon Violations | 65 | 57 | -8 | -12% |
| Offenses Against Family & Children | 16 | 14 | -2 | -12% |
| Motor Vehicle Theft | 6 | 5 | -1 | -17% |
| Burglary | 11 | 9 | -2 | -18% |
| Assault on a Police Officer | 20 | 15 | -5 | -25% |
| Sex Offenses | 6 | 4 | -2 | -33% |
| Damage to Property | 33 | 20 | -13 | -39% |
| Property Crimes | 32 | 19 | -13 | -41% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 2 | +2 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_5D_categories.png)

\newpage
## ANC 5E

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 1 | 7 | +6 | +600% |
| Driving/Boating While Intoxicated | 6 | 17 | +11 | +183% |
| Traffic Violations | 13 | 22 | +9 | +69% |
| Aggravated Assault | 3 | 5 | +2 | +67% |
| Narcotics | 8 | 10 | +2 | +25% |
| Theft | 4 | 5 | +1 | +25% |
| Robbery | 5 | 5 | +0 | 0% |
| Simple Assault | 79 | 65 | -14 | -18% |
| Other Crimes | 9 | 7 | -2 | -22% |
| Damage to Property | 14 | 10 | -4 | -29% |
| Release Violations/Fugitive | 46 | 32 | -14 | -30% |
| Offenses Against Family & Children | 9 | 6 | -3 | -33% |
| Assault with a Dangerous Weapon | 8 | 5 | -3 | -38% |
| Property Crimes | 15 | 9 | -6 | -40% |
| Weapon Violations | 29 | 14 | -15 | -52% |
| Assault on a Police Officer | 6 | 2 | -4 | -67% |
| Homicide | 5 | 0 | -5 | -100% |
| Arson | 0 | 1 | +1 | N/A |
| Burglary | 0 | 3 | +3 | N/A |
| Disorderly Conduct | 0 | 5 | +5 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 1 | +1 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 1 | +1 | N/A |
| Sex Offenses | 0 | 2 | +2 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_5E_categories.png)

\newpage
## ANC 5F

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Aggravated Assault | 1 | 8 | +7 | +700% |
| Traffic Violations | 6 | 18 | +12 | +200% |
| Theft | 7 | 15 | +8 | +114% |
| Robbery | 4 | 7 | +3 | +75% |
| Release Violations/Fugitive | 17 | 26 | +9 | +53% |
| Property Crimes | 11 | 15 | +4 | +36% |
| Other Crimes | 16 | 20 | +4 | +25% |
| Weapon Violations | 24 | 30 | +6 | +25% |
| Assault with a Dangerous Weapon | 9 | 11 | +2 | +22% |
| Narcotics | 22 | 26 | +4 | +18% |
| Driving/Boating While Intoxicated | 17 | 18 | +1 | +6% |
| Sex Abuse | 1 | 1 | +0 | 0% |
| Liquor Law Violations | 8 | 7 | -1 | -12% |
| Assault on a Police Officer | 6 | 5 | -1 | -17% |
| Simple Assault | 134 | 105 | -29 | -22% |
| Offenses Against Family & Children | 9 | 7 | -2 | -22% |
| Damage to Property | 19 | 14 | -5 | -26% |
| Burglary | 2 | 1 | -1 | -50% |
| Homicide | 2 | 1 | -1 | -50% |
| Fraud and Financial Crimes | 1 | 0 | -1 | -100% |
| Kidnapping | 2 | 0 | -2 | -100% |
| Sex Offenses | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 5 | +5 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 3 | +3 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_5F_categories.png)

\newpage
## ANC 6A

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 13 | 59 | +46 | +354% |
| Theft | 7 | 22 | +15 | +214% |
| Liquor Law Violations | 5 | 15 | +10 | +200% |
| Traffic Violations | 12 | 31 | +19 | +158% |
| Sex Offenses | 1 | 2 | +1 | +100% |
| Weapon Violations | 10 | 18 | +8 | +80% |
| Disorderly Conduct | 4 | 6 | +2 | +50% |
| Simple Assault | 52 | 55 | +3 | +6% |
| Damage to Property | 8 | 8 | +0 | 0% |
| Driving/Boating While Intoxicated | 8 | 8 | +0 | 0% |
| Offenses Against Family & Children | 4 | 4 | +0 | 0% |
| Robbery | 3 | 3 | +0 | 0% |
| Release Violations/Fugitive | 25 | 23 | -2 | -8% |
| Assault with a Dangerous Weapon | 2 | 1 | -1 | -50% |
| Property Crimes | 9 | 4 | -5 | -56% |
| Other Crimes | 16 | 7 | -9 | -56% |
| Assault on a Police Officer | 2 | 0 | -2 | -100% |
| Burglary | 2 | 0 | -2 | -100% |
| Homicide | 2 | 0 | -2 | -100% |
| Theft from Auto | 1 | 0 | -1 | -100% |
| Aggravated Assault | 0 | 3 | +3 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 1 | +1 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_6A_categories.png)

\newpage
## ANC 6B

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 3 | 29 | +26 | +867% |
| Theft | 8 | 70 | +62 | +775% |
| Assault with a Dangerous Weapon | 1 | 5 | +4 | +400% |
| Property Crimes | 7 | 14 | +7 | +100% |
| Burglary | 4 | 6 | +2 | +50% |
| Narcotics | 8 | 12 | +4 | +50% |
| Other Crimes | 12 | 15 | +3 | +25% |
| Driving/Boating While Intoxicated | 12 | 12 | +0 | 0% |
| Sex Offenses | 2 | 2 | +0 | 0% |
| Weapon Violations | 13 | 10 | -3 | -23% |
| Release Violations/Fugitive | 23 | 17 | -6 | -26% |
| Simple Assault | 63 | 39 | -24 | -38% |
| Damage to Property | 10 | 4 | -6 | -60% |
| Aggravated Assault | 3 | 1 | -2 | -67% |
| Homicide | 3 | 1 | -2 | -67% |
| Offenses Against Family & Children | 7 | 1 | -6 | -86% |
| Disorderly Conduct | 1 | 0 | -1 | -100% |
| Liquor Law Violations | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Assault on a Police Officer | 0 | 7 | +7 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Robbery | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_6B_categories.png)

\newpage
## ANC 6C

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Sex Offenses | 1 | 4 | +3 | +300% |
| Traffic Violations | 6 | 17 | +11 | +183% |
| Aggravated Assault | 3 | 5 | +2 | +67% |
| Narcotics | 5 | 8 | +3 | +60% |
| Offenses Against Family & Children | 4 | 6 | +2 | +50% |
| Release Violations/Fugitive | 12 | 14 | +2 | +17% |
| Liquor Law Violations | 1 | 1 | +0 | 0% |
| Motor Vehicle Theft | 1 | 1 | +0 | 0% |
| Property Crimes | 3 | 3 | +0 | 0% |
| Weapon Violations | 11 | 11 | +0 | 0% |
| Other Crimes | 19 | 16 | -3 | -16% |
| Theft | 20 | 16 | -4 | -20% |
| Assault on a Police Officer | 9 | 7 | -2 | -22% |
| Simple Assault | 55 | 37 | -18 | -33% |
| Robbery | 3 | 2 | -1 | -33% |
| Damage to Property | 14 | 9 | -5 | -36% |
| Driving/Boating While Intoxicated | 10 | 4 | -6 | -60% |
| Arson | 1 | 0 | -1 | -100% |
| Sex Abuse | 1 | 0 | -1 | -100% |
| Assault with a Dangerous Weapon | 0 | 1 | +1 | N/A |
| Burglary | 0 | 1 | +1 | N/A |
| Disorderly Conduct | 0 | 4 | +4 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_6C_categories.png)

\newpage
## ANC 6D

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 5 | 13 | +8 | +160% |
| Traffic Violations | 27 | 61 | +34 | +126% |
| Narcotics | 10 | 21 | +11 | +110% |
| Motor Vehicle Theft | 1 | 2 | +1 | +100% |
| Burglary | 4 | 7 | +3 | +75% |
| Robbery | 6 | 10 | +4 | +67% |
| Assault with a Dangerous Weapon | 8 | 12 | +4 | +50% |
| Aggravated Assault | 7 | 9 | +2 | +29% |
| Theft | 31 | 34 | +3 | +10% |
| Release Violations/Fugitive | 36 | 34 | -2 | -6% |
| Homicide | 26 | 24 | -2 | -8% |
| Offenses Against Family & Children | 47 | 41 | -6 | -13% |
| Weapon Violations | 22 | 19 | -3 | -14% |
| Driving/Boating While Intoxicated | 11 | 9 | -2 | -18% |
| Other Crimes | 21 | 17 | -4 | -19% |
| Simple Assault | 160 | 119 | -41 | -26% |
| Assault on a Police Officer | 7 | 5 | -2 | -29% |
| Sex Offenses | 10 | 7 | -3 | -30% |
| Property Crimes | 13 | 8 | -5 | -38% |
| Damage to Property | 18 | 9 | -9 | -50% |
| Fraud and Financial Crimes | 2 | 1 | -1 | -50% |
| Sex Abuse | 7 | 1 | -6 | -86% |
| Disorderly Conduct | 6 | 0 | -6 | -100% |
| Kidnapping | 1 | 0 | -1 | -100% |
| Prostitution | 1 | 0 | -1 | -100% |
| Vending Violations | 2 | 0 | -2 | -100% |
| Arson | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |

![](images/anc_6D_categories.png)

\newpage
## ANC 6E

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Aggravated Assault | 2 | 10 | +8 | +400% |
| Narcotics | 10 | 29 | +19 | +190% |
| Liquor Law Violations | 3 | 7 | +4 | +133% |
| Sex Offenses | 5 | 9 | +4 | +80% |
| Robbery | 7 | 12 | +5 | +71% |
| Fraud and Financial Crimes | 2 | 3 | +1 | +50% |
| Traffic Violations | 26 | 37 | +11 | +42% |
| Disorderly Conduct | 3 | 4 | +1 | +33% |
| Homicide | 6 | 8 | +2 | +33% |
| Property Crimes | 17 | 19 | +2 | +12% |
| Weapon Violations | 28 | 31 | +3 | +11% |
| Theft | 36 | 37 | +1 | +3% |
| Theft from Auto | 1 | 1 | +0 | 0% |
| Assault with a Dangerous Weapon | 11 | 10 | -1 | -9% |
| Simple Assault | 152 | 138 | -14 | -9% |
| Damage to Property | 24 | 21 | -3 | -12% |
| Assault on a Police Officer | 11 | 9 | -2 | -18% |
| Release Violations/Fugitive | 55 | 44 | -11 | -20% |
| Other Crimes | 48 | 37 | -11 | -23% |
| Driving/Boating While Intoxicated | 18 | 12 | -6 | -33% |
| Offenses Against Family & Children | 14 | 9 | -5 | -36% |
| Motor Vehicle Theft | 2 | 1 | -1 | -50% |
| Burglary | 8 | 3 | -5 | -62% |
| Sex Abuse | 3 | 1 | -2 | -67% |
| Arson | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_6E_categories.png)

\newpage
## ANC 7B

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 3 | 29 | +26 | +867% |
| Theft | 9 | 31 | +22 | +244% |
| Narcotics | 5 | 17 | +12 | +240% |
| Traffic Violations | 20 | 64 | +44 | +220% |
| Sex Offenses | 1 | 2 | +1 | +100% |
| Aggravated Assault | 4 | 7 | +3 | +75% |
| Burglary | 2 | 3 | +1 | +50% |
| Weapon Violations | 39 | 43 | +4 | +10% |
| Release Violations/Fugitive | 42 | 41 | -1 | -2% |
| Property Crimes | 25 | 24 | -1 | -4% |
| Simple Assault | 155 | 148 | -7 | -5% |
| Assault with a Dangerous Weapon | 16 | 14 | -2 | -12% |
| Other Crimes | 25 | 20 | -5 | -20% |
| Driving/Boating While Intoxicated | 16 | 12 | -4 | -25% |
| Damage to Property | 24 | 15 | -9 | -38% |
| Assault on a Police Officer | 7 | 3 | -4 | -57% |
| Offenses Against Family & Children | 13 | 5 | -8 | -62% |
| Robbery | 4 | 1 | -3 | -75% |
| Homicide | 2 | 0 | -2 | -100% |
| Kidnapping | 2 | 0 | -2 | -100% |
| Sex Abuse | 2 | 0 | -2 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 1 | +1 | N/A |
| Fraud and Financial Crimes | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_7B_categories.png)

\newpage
## ANC 7C

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 30 | 522 | +492 | +1640% |
| Liquor Law Violations | 8 | 92 | +84 | +1050% |
| Sex Offenses | 5 | 12 | +7 | +140% |
| Theft | 5 | 12 | +7 | +140% |
| Burglary | 4 | 9 | +5 | +125% |
| Disorderly Conduct | 2 | 4 | +2 | +100% |
| Offenses Against Family & Children | 17 | 23 | +6 | +35% |
| Release Violations/Fugitive | 63 | 83 | +20 | +32% |
| Assault with a Dangerous Weapon | 17 | 22 | +5 | +29% |
| Narcotics | 33 | 40 | +7 | +21% |
| Property Crimes | 24 | 25 | +1 | +4% |
| Simple Assault | 210 | 218 | +8 | +4% |
| Robbery | 14 | 14 | +0 | 0% |
| Sex Abuse | 2 | 2 | +0 | 0% |
| Assault on a Police Officer | 10 | 9 | -1 | -10% |
| Damage to Property | 27 | 24 | -3 | -11% |
| Driving/Boating While Intoxicated | 13 | 10 | -3 | -23% |
| Other Crimes | 28 | 20 | -8 | -29% |
| Homicide | 3 | 2 | -1 | -33% |
| Weapon Violations | 97 | 56 | -41 | -42% |
| Aggravated Assault | 4 | 2 | -2 | -50% |
| Kidnapping | 1 | 0 | -1 | -100% |
| Prostitution | 4 | 0 | -4 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 2 | +2 | N/A |
| Motor Vehicle Theft | 0 | 3 | +3 | N/A |
| Theft from Auto | 0 | 3 | +3 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_7C_categories.png)

\newpage
## ANC 7D

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 5 | 32 | +27 | +540% |
| Burglary | 1 | 5 | +4 | +400% |
| Traffic Violations | 24 | 95 | +71 | +296% |
| Narcotics | 21 | 63 | +42 | +200% |
| Theft | 11 | 26 | +15 | +136% |
| Assault with a Dangerous Weapon | 8 | 13 | +5 | +62% |
| Robbery | 7 | 9 | +2 | +29% |
| Aggravated Assault | 4 | 5 | +1 | +25% |
| Offenses Against Family & Children | 13 | 14 | +1 | +8% |
| Homicide | 3 | 3 | +0 | 0% |
| Property Crimes | 16 | 15 | -1 | -6% |
| Driving/Boating While Intoxicated | 17 | 15 | -2 | -12% |
| Release Violations/Fugitive | 56 | 45 | -11 | -20% |
| Simple Assault | 177 | 126 | -51 | -29% |
| Assault on a Police Officer | 6 | 4 | -2 | -33% |
| Weapon Violations | 75 | 50 | -25 | -33% |
| Sex Offenses | 5 | 3 | -2 | -40% |
| Other Crimes | 32 | 19 | -13 | -41% |
| Damage to Property | 29 | 15 | -14 | -48% |
| Kidnapping | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 4 | +4 | N/A |
| Fraud and Financial Crimes | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_7D_categories.png)

\newpage
## ANC 7E

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 7 | 104 | +97 | +1386% |
| Liquor Law Violations | 3 | 37 | +34 | +1133% |
| Theft | 3 | 9 | +6 | +200% |
| Narcotics | 13 | 31 | +18 | +138% |
| Homicide | 1 | 2 | +1 | +100% |
| Offenses Against Family & Children | 6 | 12 | +6 | +100% |
| Damage to Property | 18 | 22 | +4 | +22% |
| Property Crimes | 15 | 16 | +1 | +7% |
| Assault on a Police Officer | 4 | 4 | +0 | 0% |
| Assault with a Dangerous Weapon | 9 | 9 | +0 | 0% |
| Burglary | 2 | 2 | +0 | 0% |
| Simple Assault | 170 | 158 | -12 | -7% |
| Release Violations/Fugitive | 41 | 34 | -7 | -17% |
| Weapon Violations | 70 | 54 | -16 | -23% |
| Robbery | 5 | 3 | -2 | -40% |
| Driving/Boating While Intoxicated | 8 | 4 | -4 | -50% |
| Other Crimes | 20 | 6 | -14 | -70% |
| Kidnapping | 1 | 0 | -1 | -100% |
| Motor Vehicle Theft | 2 | 0 | -2 | -100% |
| Sex Abuse | 3 | 0 | -3 | -100% |
| Sex Offenses | 5 | 0 | -5 | -100% |
| Aggravated Assault | 0 | 7 | +7 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 2 | +2 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_7E_categories.png)

\newpage
## ANC 7F

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 19 | 362 | +343 | +1805% |
| Liquor Law Violations | 8 | 65 | +57 | +712% |
| Theft | 24 | 64 | +40 | +167% |
| Aggravated Assault | 3 | 7 | +4 | +133% |
| Fraud and Financial Crimes | 1 | 2 | +1 | +100% |
| Narcotics | 24 | 41 | +17 | +71% |
| Sex Offenses | 4 | 6 | +2 | +50% |
| Assault with a Dangerous Weapon | 54 | 72 | +18 | +33% |
| Assault on a Police Officer | 12 | 15 | +3 | +25% |
| Burglary | 8 | 9 | +1 | +12% |
| Homicide | 13 | 14 | +1 | +8% |
| Release Violations/Fugitive | 186 | 199 | +13 | +7% |
| Disorderly Conduct | 1 | 1 | +0 | 0% |
| Offenses Against Family & Children | 18 | 18 | +0 | 0% |
| Other Crimes | 36 | 32 | -4 | -11% |
| Damage to Property | 27 | 23 | -4 | -15% |
| Property Crimes | 44 | 37 | -7 | -16% |
| Simple Assault | 245 | 194 | -51 | -21% |
| Driving/Boating While Intoxicated | 15 | 11 | -4 | -27% |
| Weapon Violations | 83 | 60 | -23 | -28% |
| Robbery | 14 | 10 | -4 | -29% |
| Motor Vehicle Theft | 2 | 1 | -1 | -50% |
| Sex Abuse | 3 | 1 | -2 | -67% |
| Arson | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_7F_categories.png)

\newpage
## ANC 8A

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 3 | 73 | +70 | +2333% |
| Traffic Violations | 19 | 101 | +82 | +432% |
| Narcotics | 20 | 97 | +77 | +385% |
| Disorderly Conduct | 1 | 4 | +3 | +300% |
| Burglary | 3 | 6 | +3 | +100% |
| Theft | 7 | 14 | +7 | +100% |
| Property Crimes | 18 | 33 | +15 | +83% |
| Assault on a Police Officer | 8 | 14 | +6 | +75% |
| Sex Offenses | 3 | 5 | +2 | +67% |
| Aggravated Assault | 7 | 9 | +2 | +29% |
| Damage to Property | 21 | 27 | +6 | +29% |
| Assault with a Dangerous Weapon | 12 | 14 | +2 | +17% |
| Weapon Violations | 79 | 86 | +7 | +9% |
| Homicide | 5 | 5 | +0 | 0% |
| Other Crimes | 20 | 19 | -1 | -5% |
| Simple Assault | 206 | 189 | -17 | -8% |
| Offenses Against Family & Children | 17 | 14 | -3 | -18% |
| Driving/Boating While Intoxicated | 25 | 16 | -9 | -36% |
| Release Violations/Fugitive | 62 | 38 | -24 | -39% |
| Robbery | 10 | 6 | -4 | -40% |
| Sex Abuse | 2 | 1 | -1 | -50% |
| Prostitution | 5 | 0 | -5 | -100% |
| Arson | 0 | 1 | +1 | N/A |
| Fraud and Financial Crimes | 0 | 2 | +2 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 3 | +3 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_8A_categories.png)

\newpage
## ANC 8B

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 11 | 71 | +60 | +545% |
| Motor Vehicle Theft | 1 | 6 | +5 | +500% |
| Disorderly Conduct | 2 | 11 | +9 | +450% |
| Burglary | 2 | 9 | +7 | +350% |
| Aggravated Assault | 5 | 18 | +13 | +260% |
| Sex Abuse | 1 | 3 | +2 | +200% |
| Theft | 7 | 16 | +9 | +129% |
| Traffic Violations | 30 | 64 | +34 | +113% |
| Assault with a Dangerous Weapon | 14 | 29 | +15 | +107% |
| Assault on a Police Officer | 9 | 17 | +8 | +89% |
| Robbery | 5 | 9 | +4 | +80% |
| Other Crimes | 24 | 38 | +14 | +58% |
| Weapon Violations | 64 | 92 | +28 | +44% |
| Homicide | 3 | 4 | +1 | +33% |
| Driving/Boating While Intoxicated | 13 | 15 | +2 | +15% |
| Damage to Property | 27 | 28 | +1 | +4% |
| Simple Assault | 268 | 273 | +5 | +2% |
| Release Violations/Fugitive | 68 | 65 | -3 | -4% |
| Property Crimes | 23 | 21 | -2 | -9% |
| Offenses Against Family & Children | 25 | 17 | -8 | -32% |
| Sex Offenses | 8 | 4 | -4 | -50% |
| Kidnapping | 3 | 1 | -2 | -67% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 2 | +2 | N/A |
| Liquor Law Violations | 0 | 15 | +15 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_8B_categories.png)

\newpage
## ANC 8C

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 2 | 43 | +41 | +2050% |
| Burglary | 2 | 9 | +7 | +350% |
| Narcotics | 23 | 100 | +77 | +335% |
| Traffic Violations | 33 | 140 | +107 | +324% |
| Aggravated Assault | 7 | 14 | +7 | +100% |
| Theft | 10 | 17 | +7 | +70% |
| Property Crimes | 22 | 29 | +7 | +32% |
| Weapon Violations | 78 | 98 | +20 | +26% |
| Release Violations/Fugitive | 51 | 57 | +6 | +12% |
| Homicide | 1 | 1 | +0 | 0% |
| Other Crimes | 37 | 37 | +0 | 0% |
| Sex Offenses | 5 | 5 | +0 | 0% |
| Offenses Against Family & Children | 25 | 24 | -1 | -4% |
| Assault on a Police Officer | 27 | 25 | -2 | -7% |
| Simple Assault | 289 | 255 | -34 | -12% |
| Driving/Boating While Intoxicated | 53 | 42 | -11 | -21% |
| Assault with a Dangerous Weapon | 27 | 19 | -8 | -30% |
| Damage to Property | 33 | 20 | -13 | -39% |
| Sex Abuse | 4 | 2 | -2 | -50% |
| Robbery | 5 | 2 | -3 | -60% |
| Arson | 1 | 0 | -1 | -100% |
| Disorderly Conduct | 0 | 8 | +8 | N/A |
| Fraud and Financial Crimes | 0 | 2 | +2 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 4 | +4 | N/A |
| Prostitution | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_8C_categories.png)

\newpage
## ANC 8D

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 4 | 25 | +21 | +525% |
| Aggravated Assault | 3 | 13 | +10 | +333% |
| Theft | 4 | 14 | +10 | +250% |
| Traffic Violations | 29 | 75 | +46 | +159% |
| Assault with a Dangerous Weapon | 13 | 22 | +9 | +69% |
| Narcotics | 56 | 90 | +34 | +61% |
| Property Crimes | 19 | 30 | +11 | +58% |
| Burglary | 2 | 3 | +1 | +50% |
| Other Crimes | 37 | 53 | +16 | +43% |
| Assault on a Police Officer | 10 | 14 | +4 | +40% |
| Driving/Boating While Intoxicated | 29 | 36 | +7 | +24% |
| Sex Abuse | 2 | 2 | +0 | 0% |
| Damage to Property | 27 | 24 | -3 | -11% |
| Release Violations/Fugitive | 59 | 52 | -7 | -12% |
| Simple Assault | 234 | 185 | -49 | -21% |
| Homicide | 4 | 3 | -1 | -25% |
| Weapon Violations | 60 | 45 | -15 | -25% |
| Offenses Against Family & Children | 24 | 16 | -8 | -33% |
| Robbery | 6 | 4 | -2 | -33% |
| Disorderly Conduct | 5 | 3 | -2 | -40% |
| Sex Offenses | 4 | 1 | -3 | -75% |
| Kidnapping | 1 | 0 | -1 | -100% |
| Motor Vehicle Theft | 2 | 0 | -2 | -100% |
| Theft from Auto | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_8D_categories.png)

\newpage
## ANC 8E

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Burglary | 1 | 9 | +8 | +800% |
| Liquor Law Violations | 4 | 30 | +26 | +650% |
| Traffic Violations | 18 | 94 | +76 | +422% |
| Disorderly Conduct | 2 | 10 | +8 | +400% |
| Narcotics | 29 | 94 | +65 | +224% |
| Motor Vehicle Theft | 1 | 3 | +2 | +200% |
| Robbery | 2 | 6 | +4 | +200% |
| Sex Offenses | 2 | 6 | +4 | +200% |
| Aggravated Assault | 10 | 21 | +11 | +110% |
| Other Crimes | 48 | 77 | +29 | +60% |
| Assault on a Police Officer | 22 | 31 | +9 | +41% |
| Offenses Against Family & Children | 13 | 17 | +4 | +31% |
| Release Violations/Fugitive | 51 | 60 | +9 | +18% |
| Weapon Violations | 74 | 83 | +9 | +12% |
| Property Crimes | 28 | 30 | +2 | +7% |
| Assault with a Dangerous Weapon | 20 | 21 | +1 | +5% |
| Simple Assault | 237 | 237 | +0 | 0% |
| Theft | 21 | 20 | -1 | -5% |
| Driving/Boating While Intoxicated | 22 | 19 | -3 | -14% |
| Damage to Property | 27 | 22 | -5 | -19% |
| Homicide | 3 | 2 | -1 | -33% |
| Sex Abuse | 4 | 2 | -2 | -50% |
| Kidnapping | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 12 | +12 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/anc_8E_categories.png)

\newpage
## ANC 8F

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 1 | 9 | +8 | +800% |
| Aggravated Assault | 1 | 3 | +2 | +200% |
| Offenses Against Family & Children | 3 | 9 | +6 | +200% |
| Theft | 31 | 74 | +43 | +139% |
| Property Crimes | 4 | 7 | +3 | +75% |
| Other Crimes | 7 | 12 | +5 | +71% |
| Assault on a Police Officer | 3 | 5 | +2 | +67% |
| Simple Assault | 68 | 84 | +16 | +24% |
| Arson | 1 | 1 | +0 | 0% |
| Assault with a Dangerous Weapon | 6 | 6 | +0 | 0% |
| Burglary | 2 | 2 | +0 | 0% |
| Fraud and Financial Crimes | 1 | 1 | +0 | 0% |
| Theft from Auto | 1 | 1 | +0 | 0% |
| Traffic Violations | 35 | 33 | -2 | -6% |
| Damage to Property | 9 | 6 | -3 | -33% |
| Weapon Violations | 9 | 6 | -3 | -33% |
| Release Violations/Fugitive | 29 | 15 | -14 | -48% |
| Sex Offenses | 2 | 1 | -1 | -50% |
| Driving/Boating While Intoxicated | 18 | 6 | -12 | -67% |
| Motor Vehicle Theft | 1 | 0 | -1 | -100% |
| Vending Violations | 2 | 0 | -2 | -100% |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 1 | +1 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 5 | +5 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Robbery | 0 | 3 | +3 | N/A |
| Sex Abuse | 0 | 1 | +1 | N/A |

![](images/anc_8F_categories.png)



\newpage
# Appendix 4: Data by PSA

\newpage
## PSA 101

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Assault with a Dangerous Weapon | 1 | 3 | +2 | +200% |
| Assault on a Police Officer | 8 | 9 | +1 | +12% |
| Narcotics | 46 | 43 | -3 | -7% |
| Damage to Property | 13 | 12 | -1 | -8% |
| Simple Assault | 76 | 67 | -9 | -12% |
| Theft | 31 | 27 | -4 | -13% |
| Traffic Violations | 29 | 24 | -5 | -17% |
| Sex Offenses | 5 | 4 | -1 | -20% |
| Driving/Boating While Intoxicated | 10 | 6 | -4 | -40% |
| Weapon Violations | 22 | 13 | -9 | -41% |
| Other Crimes | 30 | 16 | -14 | -47% |
| Liquor Law Violations | 32 | 17 | -15 | -47% |
| Aggravated Assault | 2 | 1 | -1 | -50% |
| Release Violations/Fugitive | 61 | 28 | -33 | -54% |
| Burglary | 3 | 1 | -2 | -67% |
| Offenses Against Family & Children | 6 | 2 | -4 | -67% |
| Robbery | 3 | 1 | -2 | -67% |
| Property Crimes | 17 | 3 | -14 | -82% |
| Disorderly Conduct | 7 | 1 | -6 | -86% |
| Gambling | 3 | 0 | -3 | -100% |
| Homicide | 2 | 0 | -2 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 2 | +2 | N/A |
| Prostitution | 0 | 2 | +2 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_101_categories.png)

\newpage
## PSA 102

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 1 | 4 | +3 | +300% |
| Aggravated Assault | 2 | 6 | +4 | +200% |
| Traffic Violations | 9 | 22 | +13 | +144% |
| Sex Offenses | 3 | 7 | +4 | +133% |
| Robbery | 6 | 11 | +5 | +83% |
| Homicide | 4 | 7 | +3 | +75% |
| Narcotics | 9 | 15 | +6 | +67% |
| Property Crimes | 6 | 10 | +4 | +67% |
| Assault on a Police Officer | 4 | 6 | +2 | +50% |
| Theft | 9 | 13 | +4 | +44% |
| Driving/Boating While Intoxicated | 8 | 10 | +2 | +25% |
| Assault with a Dangerous Weapon | 6 | 7 | +1 | +17% |
| Arson | 1 | 1 | +0 | 0% |
| Fraud and Financial Crimes | 2 | 2 | +0 | 0% |
| Weapon Violations | 16 | 15 | -1 | -6% |
| Simple Assault | 83 | 76 | -7 | -8% |
| Offenses Against Family & Children | 11 | 10 | -1 | -9% |
| Other Crimes | 20 | 18 | -2 | -10% |
| Sex Abuse | 3 | 2 | -1 | -33% |
| Damage to Property | 20 | 12 | -8 | -40% |
| Release Violations/Fugitive | 74 | 42 | -32 | -43% |
| Burglary | 4 | 2 | -2 | -50% |
| Motor Vehicle Theft | 2 | 0 | -2 | -100% |
| Disorderly Conduct | 0 | 6 | +6 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_102_categories.png)

\newpage
## PSA 103

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Assault with a Dangerous Weapon | 1 | 4 | +3 | +300% |
| Traffic Violations | 8 | 22 | +14 | +175% |
| Motor Vehicle Theft | 1 | 2 | +1 | +100% |
| Property Crimes | 1 | 2 | +1 | +100% |
| Offenses Against Family & Children | 3 | 5 | +2 | +67% |
| Narcotics | 3 | 4 | +1 | +33% |
| Burglary | 1 | 1 | +0 | 0% |
| Theft | 7 | 7 | +0 | 0% |
| Driving/Boating While Intoxicated | 9 | 7 | -2 | -22% |
| Other Crimes | 12 | 9 | -3 | -25% |
| Simple Assault | 59 | 40 | -19 | -32% |
| Damage to Property | 3 | 2 | -1 | -33% |
| Robbery | 3 | 2 | -1 | -33% |
| Release Violations/Fugitive | 9 | 5 | -4 | -44% |
| Assault on a Police Officer | 2 | 1 | -1 | -50% |
| Sex Offenses | 2 | 1 | -1 | -50% |
| Weapon Violations | 6 | 3 | -3 | -50% |
| Aggravated Assault | 3 | 1 | -2 | -67% |
| Disorderly Conduct | 1 | 0 | -1 | -100% |
| Kidnapping | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_103_categories.png)

\newpage
## PSA 104

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 3 | 14 | +11 | +367% |
| Narcotics | 15 | 62 | +47 | +313% |
| Aggravated Assault | 1 | 4 | +3 | +300% |
| Traffic Violations | 13 | 30 | +17 | +131% |
| Motor Vehicle Theft | 1 | 2 | +1 | +100% |
| Theft | 19 | 32 | +13 | +68% |
| Weapon Violations | 11 | 17 | +6 | +55% |
| Disorderly Conduct | 4 | 6 | +2 | +50% |
| Other Crimes | 15 | 18 | +3 | +20% |
| Simple Assault | 57 | 65 | +8 | +14% |
| Assault with a Dangerous Weapon | 1 | 1 | +0 | 0% |
| Robbery | 4 | 4 | +0 | 0% |
| Sex Offenses | 2 | 2 | +0 | 0% |
| Release Violations/Fugitive | 24 | 22 | -2 | -8% |
| Damage to Property | 12 | 10 | -2 | -17% |
| Offenses Against Family & Children | 6 | 5 | -1 | -17% |
| Driving/Boating While Intoxicated | 7 | 4 | -3 | -43% |
| Burglary | 2 | 1 | -1 | -50% |
| Property Crimes | 9 | 4 | -5 | -56% |
| Assault on a Police Officer | 6 | 2 | -4 | -67% |
| Homicide | 1 | 0 | -1 | -100% |
| Theft from Auto | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_104_categories.png)

\newpage
## PSA 105

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 5 | 13 | +8 | +160% |
| Aggravated Assault | 4 | 9 | +5 | +125% |
| Narcotics | 8 | 17 | +9 | +112% |
| Burglary | 3 | 6 | +3 | +100% |
| Robbery | 4 | 8 | +4 | +100% |
| Traffic Violations | 22 | 42 | +20 | +91% |
| Theft | 24 | 28 | +4 | +17% |
| Weapon Violations | 15 | 17 | +2 | +13% |
| Release Violations/Fugitive | 29 | 30 | +1 | +3% |
| Assault with a Dangerous Weapon | 8 | 8 | +0 | 0% |
| Other Crimes | 8 | 8 | +0 | 0% |
| Homicide | 26 | 24 | -2 | -8% |
| Simple Assault | 102 | 85 | -17 | -17% |
| Offenses Against Family & Children | 44 | 36 | -8 | -18% |
| Sex Offenses | 8 | 6 | -2 | -25% |
| Driving/Boating While Intoxicated | 8 | 5 | -3 | -38% |
| Assault on a Police Officer | 5 | 3 | -2 | -40% |
| Fraud and Financial Crimes | 2 | 1 | -1 | -50% |
| Property Crimes | 12 | 6 | -6 | -50% |
| Damage to Property | 16 | 7 | -9 | -56% |
| Disorderly Conduct | 5 | 0 | -5 | -100% |
| Motor Vehicle Theft | 1 | 0 | -1 | -100% |
| Prostitution | 1 | 0 | -1 | -100% |
| Sex Abuse | 7 | 0 | -7 | -100% |
| Vending Violations | 4 | 0 | -4 | -100% |
| Arson | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |

![](images/psa_105_categories.png)

\newpage
## PSA 106

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 6 | 20 | +14 | +233% |
| Theft | 33 | 100 | +67 | +203% |
| Assault on a Police Officer | 3 | 7 | +4 | +133% |
| Offenses Against Family & Children | 4 | 9 | +5 | +125% |
| Homicide | 1 | 2 | +1 | +100% |
| Property Crimes | 9 | 18 | +9 | +100% |
| Assault with a Dangerous Weapon | 5 | 9 | +4 | +80% |
| Sex Offenses | 2 | 3 | +1 | +50% |
| Other Crimes | 14 | 19 | +5 | +36% |
| Burglary | 5 | 6 | +1 | +20% |
| Traffic Violations | 32 | 38 | +6 | +19% |
| Arson | 1 | 1 | +0 | 0% |
| Fraud and Financial Crimes | 1 | 1 | +0 | 0% |
| Simple Assault | 99 | 99 | +0 | 0% |
| Theft from Auto | 1 | 1 | +0 | 0% |
| Weapon Violations | 18 | 11 | -7 | -39% |
| Release Violations/Fugitive | 47 | 27 | -20 | -43% |
| Driving/Boating While Intoxicated | 20 | 11 | -9 | -45% |
| Damage to Property | 17 | 9 | -8 | -47% |
| Aggravated Assault | 4 | 2 | -2 | -50% |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 3 | +3 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Robbery | 0 | 2 | +2 | N/A |
| Sex Abuse | 0 | 2 | +2 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_106_categories.png)

\newpage
## PSA 107

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 4 | 29 | +25 | +625% |
| Aggravated Assault | 1 | 5 | +4 | +400% |
| Theft | 16 | 63 | +47 | +294% |
| Assault on a Police Officer | 4 | 9 | +5 | +125% |
| Weapon Violations | 5 | 9 | +4 | +80% |
| Assault with a Dangerous Weapon | 42 | 57 | +15 | +36% |
| Driving/Boating While Intoxicated | 5 | 6 | +1 | +20% |
| Release Violations/Fugitive | 147 | 167 | +20 | +14% |
| Disorderly Conduct | 1 | 1 | +0 | 0% |
| Liquor Law Violations | 1 | 1 | +0 | 0% |
| Narcotics | 5 | 5 | +0 | 0% |
| Burglary | 7 | 6 | -1 | -14% |
| Other Crimes | 17 | 14 | -3 | -18% |
| Property Crimes | 5 | 4 | -1 | -20% |
| Homicide | 14 | 11 | -3 | -21% |
| Simple Assault | 78 | 61 | -17 | -22% |
| Robbery | 6 | 4 | -2 | -33% |
| Damage to Property | 9 | 5 | -4 | -44% |
| Sex Abuse | 2 | 1 | -1 | -50% |
| Sex Offenses | 6 | 3 | -3 | -50% |
| Offenses Against Family & Children | 19 | 8 | -11 | -58% |
| Motor Vehicle Theft | 2 | 0 | -2 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_107_categories.png)

\newpage
## PSA 108

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 5 | 14 | +9 | +180% |
| Weapon Violations | 4 | 7 | +3 | +75% |
| Aggravated Assault | 2 | 3 | +1 | +50% |
| Damage to Property | 3 | 3 | +0 | 0% |
| Driving/Boating While Intoxicated | 4 | 4 | +0 | 0% |
| Narcotics | 2 | 2 | +0 | 0% |
| Property Crimes | 1 | 1 | +0 | 0% |
| Release Violations/Fugitive | 7 | 6 | -1 | -14% |
| Simple Assault | 20 | 14 | -6 | -30% |
| Other Crimes | 8 | 2 | -6 | -75% |
| Homicide | 1 | 0 | -1 | -100% |
| Robbery | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Assault on a Police Officer | 0 | 0 | +0 | N/A |
| Assault with a Dangerous Weapon | 0 | 1 | +1 | N/A |
| Burglary | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 1 | +1 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Offenses Against Family & Children | 0 | 2 | +2 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Sex Offenses | 0 | 2 | +2 | N/A |
| Theft | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_108_categories.png)

\newpage
## PSA 201

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Release Violations/Fugitive | 3 | 7 | +4 | +133% |
| Driving/Boating While Intoxicated | 3 | 4 | +1 | +33% |
| Assault with a Dangerous Weapon | 1 | 1 | +0 | 0% |
| Other Crimes | 3 | 2 | -1 | -33% |
| Simple Assault | 12 | 7 | -5 | -42% |
| Traffic Violations | 6 | 1 | -5 | -83% |
| Burglary | 2 | 0 | -2 | -100% |
| Damage to Property | 1 | 0 | -1 | -100% |
| Weapon Violations | 1 | 0 | -1 | -100% |
| Aggravated Assault | 0 | 0 | +0 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Assault on a Police Officer | 0 | 1 | +1 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Narcotics | 0 | 0 | +0 | N/A |
| Offenses Against Family & Children | 0 | 2 | +2 | N/A |
| Property Crimes | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Robbery | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Sex Offenses | 0 | 0 | +0 | N/A |
| Theft | 0 | 3 | +3 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_201_categories.png)

\newpage
## PSA 202

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Driving/Boating While Intoxicated | 2 | 5 | +3 | +150% |
| Weapon Violations | 2 | 4 | +2 | +100% |
| Release Violations/Fugitive | 4 | 5 | +1 | +25% |
| Theft | 21 | 26 | +5 | +24% |
| Assault with a Dangerous Weapon | 1 | 1 | +0 | 0% |
| Sex Offenses | 1 | 1 | +0 | 0% |
| Simple Assault | 13 | 13 | +0 | 0% |
| Damage to Property | 6 | 5 | -1 | -17% |
| Offenses Against Family & Children | 2 | 1 | -1 | -50% |
| Other Crimes | 8 | 2 | -6 | -75% |
| Aggravated Assault | 1 | 0 | -1 | -100% |
| Motor Vehicle Theft | 1 | 0 | -1 | -100% |
| Property Crimes | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Assault on a Police Officer | 0 | 1 | +1 | N/A |
| Burglary | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 1 | +1 | N/A |
| Narcotics | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Robbery | 0 | 2 | +2 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |
| Traffic Violations | 0 | 5 | +5 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_202_categories.png)

\newpage
## PSA 203

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Driving/Boating While Intoxicated | 3 | 5 | +2 | +67% |
| Assault on a Police Officer | 3 | 4 | +1 | +33% |
| Damage to Property | 6 | 8 | +2 | +33% |
| Other Crimes | 9 | 12 | +3 | +33% |
| Release Violations/Fugitive | 10 | 11 | +1 | +10% |
| Burglary | 1 | 1 | +0 | 0% |
| Offenses Against Family & Children | 5 | 5 | +0 | 0% |
| Traffic Violations | 8 | 8 | +0 | 0% |
| Weapon Violations | 2 | 2 | +0 | 0% |
| Theft | 48 | 42 | -6 | -12% |
| Simple Assault | 58 | 47 | -11 | -19% |
| Sex Offenses | 3 | 2 | -1 | -33% |
| Assault with a Dangerous Weapon | 6 | 3 | -3 | -50% |
| Narcotics | 2 | 1 | -1 | -50% |
| Property Crimes | 2 | 1 | -1 | -50% |
| Liquor Law Violations | 1 | 0 | -1 | -100% |
| Motor Vehicle Theft | 1 | 0 | -1 | -100% |
| Robbery | 1 | 0 | -1 | -100% |
| Aggravated Assault | 0 | 1 | +1 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_203_categories.png)

\newpage
## PSA 204

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Aggravated Assault | 1 | 3 | +2 | +200% |
| Assault on a Police Officer | 1 | 3 | +2 | +200% |
| Sex Offenses | 1 | 3 | +2 | +200% |
| Traffic Violations | 6 | 17 | +11 | +183% |
| Disorderly Conduct | 1 | 2 | +1 | +100% |
| Theft | 22 | 34 | +12 | +55% |
| Assault with a Dangerous Weapon | 5 | 7 | +2 | +40% |
| Offenses Against Family & Children | 3 | 3 | +0 | 0% |
| Other Crimes | 13 | 13 | +0 | 0% |
| Property Crimes | 1 | 1 | +0 | 0% |
| Release Violations/Fugitive | 16 | 15 | -1 | -6% |
| Simple Assault | 65 | 50 | -15 | -23% |
| Weapon Violations | 8 | 6 | -2 | -25% |
| Damage to Property | 7 | 4 | -3 | -43% |
| Driving/Boating While Intoxicated | 8 | 4 | -4 | -50% |
| Robbery | 8 | 4 | -4 | -50% |
| Burglary | 4 | 1 | -3 | -75% |
| Arson | 1 | 0 | -1 | -100% |
| Narcotics | 1 | 0 | -1 | -100% |
| Theft from Auto | 1 | 0 | -1 | -100% |
| Vending Violations | 2 | 0 | -2 | -100% |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 1 | +1 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 2 | +2 | N/A |

![](images/psa_204_categories.png)

\newpage
## PSA 205

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Damage to Property | 1 | 2 | +1 | +100% |
| Traffic Violations | 2 | 4 | +2 | +100% |
| Other Crimes | 3 | 5 | +2 | +67% |
| Driving/Boating While Intoxicated | 2 | 3 | +1 | +50% |
| Simple Assault | 15 | 16 | +1 | +7% |
| Property Crimes | 1 | 1 | +0 | 0% |
| Theft | 2 | 2 | +0 | 0% |
| Release Violations/Fugitive | 7 | 5 | -2 | -29% |
| Theft from Auto | 2 | 1 | -1 | -50% |
| Assault with a Dangerous Weapon | 3 | 1 | -2 | -67% |
| Offenses Against Family & Children | 3 | 1 | -2 | -67% |
| Sex Abuse | 1 | 0 | -1 | -100% |
| Aggravated Assault | 0 | 1 | +1 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Assault on a Police Officer | 0 | 2 | +2 | N/A |
| Burglary | 0 | 1 | +1 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 1 | +1 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Narcotics | 0 | 2 | +2 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Robbery | 0 | 0 | +0 | N/A |
| Sex Offenses | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |
| Weapon Violations | 0 | 0 | +0 | N/A |

![](images/psa_205_categories.png)

\newpage
## PSA 206

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 3 | 19 | +16 | +533% |
| Release Violations/Fugitive | 7 | 18 | +11 | +157% |
| Theft | 12 | 29 | +17 | +142% |
| Assault with a Dangerous Weapon | 1 | 2 | +1 | +100% |
| Damage to Property | 6 | 8 | +2 | +33% |
| Property Crimes | 4 | 5 | +1 | +25% |
| Simple Assault | 24 | 29 | +5 | +21% |
| Driving/Boating While Intoxicated | 5 | 6 | +1 | +20% |
| Other Crimes | 16 | 18 | +2 | +12% |
| Liquor Law Violations | 1 | 1 | +0 | 0% |
| Sex Offenses | 1 | 1 | +0 | 0% |
| Weapon Violations | 2 | 2 | +0 | 0% |
| Robbery | 2 | 1 | -1 | -50% |
| Assault on a Police Officer | 5 | 2 | -3 | -60% |
| Burglary | 3 | 0 | -3 | -100% |
| Fraud and Financial Crimes | 3 | 0 | -3 | -100% |
| Offenses Against Family & Children | 2 | 0 | -2 | -100% |
| Aggravated Assault | 0 | 0 | +0 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Narcotics | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_206_categories.png)

\newpage
## PSA 207

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Offenses Against Family & Children | 2 | 6 | +4 | +200% |
| Theft | 24 | 49 | +25 | +104% |
| Fraud and Financial Crimes | 2 | 4 | +2 | +100% |
| Liquor Law Violations | 2 | 4 | +2 | +100% |
| Other Crimes | 34 | 63 | +29 | +85% |
| Assault on a Police Officer | 6 | 9 | +3 | +50% |
| Property Crimes | 6 | 9 | +3 | +50% |
| Traffic Violations | 33 | 46 | +13 | +39% |
| Disorderly Conduct | 4 | 5 | +1 | +25% |
| Driving/Boating While Intoxicated | 18 | 20 | +2 | +11% |
| Aggravated Assault | 3 | 3 | +0 | 0% |
| Release Violations/Fugitive | 29 | 26 | -3 | -10% |
| Simple Assault | 87 | 71 | -16 | -18% |
| Burglary | 3 | 2 | -1 | -33% |
| Damage to Property | 12 | 7 | -5 | -42% |
| Assault with a Dangerous Weapon | 10 | 5 | -5 | -50% |
| Weapon Violations | 54 | 21 | -33 | -61% |
| Narcotics | 5 | 1 | -4 | -80% |
| Sex Offenses | 7 | 1 | -6 | -86% |
| Motor Vehicle Theft | 2 | 0 | -2 | -100% |
| Sex Abuse | 3 | 0 | -3 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 1 | +1 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Robbery | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_207_categories.png)

\newpage
## PSA 208

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 2 | 4 | +2 | +100% |
| Offenses Against Family & Children | 2 | 3 | +1 | +50% |
| Robbery | 2 | 3 | +1 | +50% |
| Sex Offenses | 2 | 3 | +1 | +50% |
| Assault on a Police Officer | 6 | 7 | +1 | +17% |
| Damage to Property | 9 | 10 | +1 | +11% |
| Theft | 45 | 50 | +5 | +11% |
| Traffic Violations | 47 | 45 | -2 | -4% |
| Driving/Boating While Intoxicated | 14 | 12 | -2 | -14% |
| Property Crimes | 8 | 6 | -2 | -25% |
| Assault with a Dangerous Weapon | 7 | 5 | -2 | -29% |
| Disorderly Conduct | 9 | 6 | -3 | -33% |
| Simple Assault | 91 | 60 | -31 | -34% |
| Weapon Violations | 58 | 37 | -21 | -36% |
| Release Violations/Fugitive | 15 | 8 | -7 | -47% |
| Other Crimes | 26 | 8 | -18 | -69% |
| Aggravated Assault | 2 | 0 | -2 | -100% |
| Burglary | 1 | 0 | -1 | -100% |
| Fraud and Financial Crimes | 4 | 0 | -4 | -100% |
| Kidnapping | 1 | 0 | -1 | -100% |
| Motor Vehicle Theft | 1 | 0 | -1 | -100% |
| Narcotics | 4 | 0 | -4 | -100% |
| Sex Abuse | 2 | 0 | -2 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_208_categories.png)

\newpage
## PSA 209

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Assault with a Dangerous Weapon | 1 | 5 | +4 | +400% |
| Aggravated Assault | 1 | 3 | +2 | +200% |
| Burglary | 1 | 3 | +2 | +200% |
| Release Violations/Fugitive | 8 | 16 | +8 | +100% |
| Theft | 41 | 81 | +40 | +98% |
| Traffic Violations | 12 | 17 | +5 | +42% |
| Weapon Violations | 13 | 14 | +1 | +8% |
| Simple Assault | 50 | 52 | +2 | +4% |
| Driving/Boating While Intoxicated | 8 | 8 | +0 | 0% |
| Property Crimes | 1 | 1 | +0 | 0% |
| Robbery | 2 | 2 | +0 | 0% |
| Damage to Property | 5 | 4 | -1 | -20% |
| Assault on a Police Officer | 6 | 4 | -2 | -33% |
| Fraud and Financial Crimes | 2 | 1 | -1 | -50% |
| Sex Offenses | 2 | 1 | -1 | -50% |
| Other Crimes | 30 | 12 | -18 | -60% |
| Disorderly Conduct | 3 | 0 | -3 | -100% |
| Motor Vehicle Theft | 2 | 0 | -2 | -100% |
| Narcotics | 2 | 0 | -2 | -100% |
| Offenses Against Family & Children | 2 | 0 | -2 | -100% |
| Vending Violations | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 1 | +1 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |

![](images/psa_209_categories.png)

\newpage
## PSA 301

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 1 | 13 | +12 | +1200% |
| Assault on a Police Officer | 1 | 7 | +6 | +600% |
| Disorderly Conduct | 1 | 5 | +4 | +400% |
| Narcotics | 3 | 8 | +5 | +167% |
| Aggravated Assault | 3 | 6 | +3 | +100% |
| Theft | 11 | 21 | +10 | +91% |
| Other Crimes | 12 | 22 | +10 | +83% |
| Release Violations/Fugitive | 15 | 27 | +12 | +80% |
| Traffic Violations | 24 | 38 | +14 | +58% |
| Robbery | 4 | 6 | +2 | +50% |
| Weapon Violations | 14 | 20 | +6 | +43% |
| Driving/Boating While Intoxicated | 7 | 9 | +2 | +29% |
| Assault with a Dangerous Weapon | 7 | 8 | +1 | +14% |
| Burglary | 1 | 1 | +0 | 0% |
| Offenses Against Family & Children | 4 | 4 | +0 | 0% |
| Sex Offenses | 1 | 1 | +0 | 0% |
| Simple Assault | 48 | 45 | -3 | -6% |
| Damage to Property | 7 | 6 | -1 | -14% |
| Property Crimes | 7 | 1 | -6 | -86% |
| Arson | 1 | 0 | -1 | -100% |
| Homicide | 1 | 0 | -1 | -100% |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 3 | +3 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_301_categories.png)

\newpage
## PSA 302

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 14 | 74 | +60 | +429% |
| Traffic Violations | 15 | 61 | +46 | +307% |
| Narcotics | 13 | 49 | +36 | +277% |
| Theft | 113 | 359 | +246 | +218% |
| Disorderly Conduct | 5 | 13 | +8 | +160% |
| Burglary | 2 | 5 | +3 | +150% |
| Robbery | 4 | 10 | +6 | +150% |
| Release Violations/Fugitive | 24 | 42 | +18 | +75% |
| Assault on a Police Officer | 12 | 18 | +6 | +50% |
| Offenses Against Family & Children | 9 | 13 | +4 | +44% |
| Damage to Property | 10 | 14 | +4 | +40% |
| Simple Assault | 122 | 129 | +7 | +6% |
| Aggravated Assault | 6 | 6 | +0 | 0% |
| Other Crimes | 62 | 54 | -8 | -13% |
| Weapon Violations | 29 | 25 | -4 | -14% |
| Driving/Boating While Intoxicated | 10 | 8 | -2 | -20% |
| Property Crimes | 8 | 6 | -2 | -25% |
| Assault with a Dangerous Weapon | 19 | 13 | -6 | -32% |
| Kidnapping | 2 | 1 | -1 | -50% |
| Sex Offenses | 8 | 3 | -5 | -62% |
| Fraud and Financial Crimes | 1 | 0 | -1 | -100% |
| Homicide | 2 | 0 | -2 | -100% |
| Sex Abuse | 2 | 0 | -2 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_302_categories.png)

\newpage
## PSA 303

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 1 | 27 | +26 | +2600% |
| Traffic Violations | 5 | 21 | +16 | +320% |
| Disorderly Conduct | 1 | 4 | +3 | +300% |
| Narcotics | 4 | 16 | +12 | +300% |
| Burglary | 2 | 5 | +3 | +150% |
| Aggravated Assault | 3 | 6 | +3 | +100% |
| Sex Abuse | 1 | 2 | +1 | +100% |
| Sex Offenses | 3 | 5 | +2 | +67% |
| Theft | 24 | 37 | +13 | +54% |
| Release Violations/Fugitive | 13 | 19 | +6 | +46% |
| Assault with a Dangerous Weapon | 3 | 4 | +1 | +33% |
| Other Crimes | 21 | 23 | +2 | +10% |
| Simple Assault | 76 | 58 | -18 | -24% |
| Driving/Boating While Intoxicated | 8 | 6 | -2 | -25% |
| Robbery | 3 | 2 | -1 | -33% |
| Weapon Violations | 8 | 5 | -3 | -38% |
| Damage to Property | 16 | 7 | -9 | -56% |
| Assault on a Police Officer | 5 | 2 | -3 | -60% |
| Offenses Against Family & Children | 5 | 2 | -3 | -60% |
| Gambling | 2 | 0 | -2 | -100% |
| Property Crimes | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_303_categories.png)

\newpage
## PSA 304

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Robbery | 1 | 7 | +6 | +600% |
| Property Crimes | 1 | 6 | +5 | +500% |
| Traffic Violations | 12 | 31 | +19 | +158% |
| Release Violations/Fugitive | 6 | 13 | +7 | +117% |
| Damage to Property | 4 | 8 | +4 | +100% |
| Assault with a Dangerous Weapon | 3 | 5 | +2 | +67% |
| Aggravated Assault | 2 | 3 | +1 | +50% |
| Assault on a Police Officer | 2 | 3 | +1 | +50% |
| Liquor Law Violations | 2 | 3 | +1 | +50% |
| Theft | 7 | 8 | +1 | +14% |
| Simple Assault | 58 | 61 | +3 | +5% |
| Sex Offenses | 2 | 2 | +0 | 0% |
| Weapon Violations | 27 | 22 | -5 | -19% |
| Other Crimes | 12 | 8 | -4 | -33% |
| Driving/Boating While Intoxicated | 15 | 9 | -6 | -40% |
| Burglary | 5 | 2 | -3 | -60% |
| Disorderly Conduct | 2 | 0 | -2 | -100% |
| Offenses Against Family & Children | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 1 | +1 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 2 | +2 | N/A |
| Narcotics | 0 | 22 | +22 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 2 | +2 | N/A |
| Theft from Auto | 0 | 2 | +2 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_304_categories.png)

\newpage
## PSA 305

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 13 | 90 | +77 | +592% |
| Liquor Law Violations | 9 | 56 | +47 | +522% |
| Robbery | 5 | 16 | +11 | +220% |
| Theft | 20 | 59 | +39 | +195% |
| Release Violations/Fugitive | 17 | 49 | +32 | +188% |
| Damage to Property | 5 | 14 | +9 | +180% |
| Disorderly Conduct | 24 | 55 | +31 | +129% |
| Motor Vehicle Theft | 1 | 2 | +1 | +100% |
| Driving/Boating While Intoxicated | 16 | 29 | +13 | +81% |
| Weapon Violations | 54 | 97 | +43 | +80% |
| Other Crimes | 33 | 59 | +26 | +79% |
| Traffic Violations | 28 | 43 | +15 | +54% |
| Property Crimes | 8 | 12 | +4 | +50% |
| Sex Offenses | 2 | 3 | +1 | +50% |
| Theft from Auto | 2 | 3 | +1 | +50% |
| Assault on a Police Officer | 13 | 18 | +5 | +38% |
| Simple Assault | 84 | 114 | +30 | +36% |
| Burglary | 4 | 4 | +0 | 0% |
| Offenses Against Family & Children | 4 | 4 | +0 | 0% |
| Sex Abuse | 1 | 1 | +0 | 0% |
| Assault with a Dangerous Weapon | 8 | 4 | -4 | -50% |
| Fraud and Financial Crimes | 3 | 1 | -2 | -67% |
| Aggravated Assault | 0 | 2 | +2 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Gambling | 0 | 1 | +1 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_305_categories.png)

\newpage
## PSA 306

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Disorderly Conduct | 1 | 7 | +6 | +600% |
| Narcotics | 13 | 78 | +65 | +500% |
| Release Violations/Fugitive | 18 | 47 | +29 | +161% |
| Theft | 10 | 26 | +16 | +160% |
| Robbery | 3 | 7 | +4 | +133% |
| Liquor Law Violations | 13 | 30 | +17 | +131% |
| Other Crimes | 7 | 16 | +9 | +129% |
| Aggravated Assault | 1 | 2 | +1 | +100% |
| Property Crimes | 6 | 12 | +6 | +100% |
| Traffic Violations | 10 | 18 | +8 | +80% |
| Assault on a Police Officer | 6 | 9 | +3 | +50% |
| Offenses Against Family & Children | 2 | 3 | +1 | +50% |
| Driving/Boating While Intoxicated | 8 | 10 | +2 | +25% |
| Simple Assault | 42 | 46 | +4 | +10% |
| Assault with a Dangerous Weapon | 9 | 7 | -2 | -22% |
| Weapon Violations | 21 | 13 | -8 | -38% |
| Burglary | 2 | 1 | -1 | -50% |
| Damage to Property | 13 | 6 | -7 | -54% |
| Homicide | 1 | 0 | -1 | -100% |
| Sex Offenses | 1 | 0 | -1 | -100% |
| Theft from Auto | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_306_categories.png)

\newpage
## PSA 307

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Damage to Property | 1 | 7 | +6 | +600% |
| Narcotics | 2 | 13 | +11 | +550% |
| Aggravated Assault | 1 | 4 | +3 | +300% |
| Offenses Against Family & Children | 2 | 7 | +5 | +250% |
| Assault with a Dangerous Weapon | 2 | 5 | +3 | +150% |
| Other Crimes | 8 | 16 | +8 | +100% |
| Theft | 19 | 35 | +16 | +84% |
| Release Violations/Fugitive | 13 | 22 | +9 | +69% |
| Weapon Violations | 10 | 15 | +5 | +50% |
| Driving/Boating While Intoxicated | 9 | 10 | +1 | +11% |
| Traffic Violations | 19 | 19 | +0 | 0% |
| Simple Assault | 64 | 58 | -6 | -9% |
| Property Crimes | 9 | 8 | -1 | -11% |
| Disorderly Conduct | 4 | 2 | -2 | -50% |
| Assault on a Police Officer | 7 | 3 | -4 | -57% |
| Arson | 1 | 0 | -1 | -100% |
| Burglary | 1 | 0 | -1 | -100% |
| Homicide | 1 | 0 | -1 | -100% |
| Theft from Auto | 1 | 0 | -1 | -100% |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 12 | +12 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 4 | +4 | N/A |
| Robbery | 0 | 5 | +5 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Sex Offenses | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_307_categories.png)

\newpage
## PSA 308

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 9 | 29 | +20 | +222% |
| Narcotics | 14 | 38 | +24 | +171% |
| Robbery | 2 | 5 | +3 | +150% |
| Driving/Boating While Intoxicated | 10 | 19 | +9 | +90% |
| Theft | 4 | 7 | +3 | +75% |
| Traffic Violations | 13 | 22 | +9 | +69% |
| Other Crimes | 15 | 17 | +2 | +13% |
| Aggravated Assault | 4 | 4 | +0 | 0% |
| Damage to Property | 9 | 9 | +0 | 0% |
| Motor Vehicle Theft | 1 | 1 | +0 | 0% |
| Simple Assault | 79 | 71 | -8 | -10% |
| Release Violations/Fugitive | 18 | 15 | -3 | -17% |
| Homicide | 3 | 2 | -1 | -33% |
| Offenses Against Family & Children | 6 | 4 | -2 | -33% |
| Property Crimes | 26 | 15 | -11 | -42% |
| Assault on a Police Officer | 4 | 2 | -2 | -50% |
| Assault with a Dangerous Weapon | 2 | 1 | -1 | -50% |
| Weapon Violations | 40 | 19 | -21 | -52% |
| Arson | 0 | 0 | +0 | N/A |
| Burglary | 0 | 3 | +3 | N/A |
| Disorderly Conduct | 0 | 4 | +4 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 1 | +1 | N/A |
| Sex Offenses | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_308_categories.png)

\newpage
## PSA 401

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 2 | 18 | +16 | +800% |
| Theft | 5 | 20 | +15 | +300% |
| Narcotics | 1 | 3 | +2 | +200% |
| Assault with a Dangerous Weapon | 2 | 4 | +2 | +100% |
| Weapon Violations | 3 | 6 | +3 | +100% |
| Damage to Property | 4 | 7 | +3 | +75% |
| Other Crimes | 5 | 8 | +3 | +60% |
| Simple Assault | 30 | 46 | +16 | +53% |
| Release Violations/Fugitive | 8 | 11 | +3 | +38% |
| Burglary | 1 | 1 | +0 | 0% |
| Robbery | 1 | 1 | +0 | 0% |
| Driving/Boating While Intoxicated | 9 | 7 | -2 | -22% |
| Offenses Against Family & Children | 3 | 2 | -1 | -33% |
| Property Crimes | 5 | 3 | -2 | -40% |
| Assault on a Police Officer | 2 | 1 | -1 | -50% |
| Homicide | 1 | 0 | -1 | -100% |
| Aggravated Assault | 0 | 0 | +0 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Sex Offenses | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_401_categories.png)

\newpage
## PSA 402

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Theft | 7 | 39 | +32 | +457% |
| Narcotics | 2 | 10 | +8 | +400% |
| Fraud and Financial Crimes | 1 | 2 | +1 | +100% |
| Traffic Violations | 21 | 32 | +11 | +52% |
| Disorderly Conduct | 2 | 3 | +1 | +50% |
| Property Crimes | 2 | 3 | +1 | +50% |
| Driving/Boating While Intoxicated | 8 | 10 | +2 | +25% |
| Other Crimes | 12 | 13 | +1 | +8% |
| Release Violations/Fugitive | 24 | 25 | +1 | +4% |
| Assault with a Dangerous Weapon | 3 | 3 | +0 | 0% |
| Motor Vehicle Theft | 1 | 1 | +0 | 0% |
| Sex Abuse | 1 | 1 | +0 | 0% |
| Simple Assault | 72 | 69 | -3 | -4% |
| Damage to Property | 6 | 5 | -1 | -17% |
| Robbery | 4 | 3 | -1 | -25% |
| Weapon Violations | 7 | 5 | -2 | -29% |
| Sex Offenses | 3 | 2 | -1 | -33% |
| Offenses Against Family & Children | 8 | 5 | -3 | -38% |
| Assault on a Police Officer | 6 | 3 | -3 | -50% |
| Burglary | 2 | 1 | -1 | -50% |
| Aggravated Assault | 5 | 2 | -3 | -60% |
| Arson | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 7 | +7 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_402_categories.png)

\newpage
## PSA 403

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Sex Offenses | 1 | 5 | +4 | +400% |
| Burglary | 1 | 4 | +3 | +300% |
| Liquor Law Violations | 2 | 6 | +4 | +200% |
| Theft | 4 | 9 | +5 | +125% |
| Aggravated Assault | 3 | 6 | +3 | +100% |
| Weapon Violations | 12 | 15 | +3 | +25% |
| Assault with a Dangerous Weapon | 5 | 6 | +1 | +20% |
| Release Violations/Fugitive | 13 | 15 | +2 | +15% |
| Simple Assault | 72 | 73 | +1 | +1% |
| Assault on a Police Officer | 3 | 3 | +0 | 0% |
| Damage to Property | 7 | 7 | +0 | 0% |
| Traffic Violations | 40 | 40 | +0 | 0% |
| Driving/Boating While Intoxicated | 16 | 14 | -2 | -12% |
| Other Crimes | 11 | 8 | -3 | -27% |
| Property Crimes | 7 | 5 | -2 | -29% |
| Narcotics | 14 | 9 | -5 | -36% |
| Offenses Against Family & Children | 8 | 5 | -3 | -38% |
| Robbery | 5 | 1 | -4 | -80% |
| Sex Abuse | 2 | 0 | -2 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 2 | +2 | N/A |
| Fraud and Financial Crimes | 0 | 3 | +3 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_403_categories.png)

\newpage
## PSA 404

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Theft | 6 | 29 | +23 | +383% |
| Burglary | 2 | 5 | +3 | +150% |
| Traffic Violations | 30 | 67 | +37 | +123% |
| Motor Vehicle Theft | 1 | 2 | +1 | +100% |
| Robbery | 4 | 8 | +4 | +100% |
| Driving/Boating While Intoxicated | 9 | 14 | +5 | +56% |
| Liquor Law Violations | 2 | 3 | +1 | +50% |
| Offenses Against Family & Children | 4 | 5 | +1 | +25% |
| Property Crimes | 8 | 10 | +2 | +25% |
| Release Violations/Fugitive | 51 | 55 | +4 | +8% |
| Assault on a Police Officer | 1 | 1 | +0 | 0% |
| Assault with a Dangerous Weapon | 6 | 6 | +0 | 0% |
| Sex Offenses | 1 | 1 | +0 | 0% |
| Simple Assault | 91 | 74 | -17 | -19% |
| Damage to Property | 15 | 11 | -4 | -27% |
| Other Crimes | 42 | 29 | -13 | -31% |
| Aggravated Assault | 3 | 2 | -1 | -33% |
| Weapon Violations | 40 | 12 | -28 | -70% |
| Narcotics | 25 | 7 | -18 | -72% |
| Homicide | 1 | 0 | -1 | -100% |
| Sex Abuse | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 3 | +3 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 2 | +2 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_404_categories.png)

\newpage
## PSA 405

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 9 | 33 | +24 | +267% |
| Aggravated Assault | 1 | 2 | +1 | +100% |
| Theft | 2 | 4 | +2 | +100% |
| Weapon Violations | 15 | 19 | +4 | +27% |
| Sex Offenses | 3 | 3 | +0 | 0% |
| Driving/Boating While Intoxicated | 9 | 7 | -2 | -22% |
| Simple Assault | 91 | 70 | -21 | -23% |
| Property Crimes | 7 | 5 | -2 | -29% |
| Assault with a Dangerous Weapon | 9 | 6 | -3 | -33% |
| Other Crimes | 12 | 8 | -4 | -33% |
| Offenses Against Family & Children | 10 | 6 | -4 | -40% |
| Release Violations/Fugitive | 48 | 25 | -23 | -48% |
| Damage to Property | 7 | 3 | -4 | -57% |
| Homicide | 3 | 1 | -2 | -67% |
| Robbery | 4 | 1 | -3 | -75% |
| Assault on a Police Officer | 7 | 1 | -6 | -86% |
| Disorderly Conduct | 2 | 0 | -2 | -100% |
| Narcotics | 5 | 0 | -5 | -100% |
| Sex Abuse | 2 | 0 | -2 | -100% |
| Arson | 0 | 1 | +1 | N/A |
| Burglary | 0 | 2 | +2 | N/A |
| Fraud and Financial Crimes | 0 | 2 | +2 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 1 | +1 | N/A |
| Liquor Law Violations | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_405_categories.png)

\newpage
## PSA 406

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 1 | 3 | +2 | +200% |
| Driving/Boating While Intoxicated | 9 | 15 | +6 | +67% |
| Theft | 10 | 16 | +6 | +60% |
| Narcotics | 2 | 3 | +1 | +50% |
| Traffic Violations | 12 | 18 | +6 | +50% |
| Release Violations/Fugitive | 15 | 20 | +5 | +33% |
| Property Crimes | 4 | 5 | +1 | +25% |
| Aggravated Assault | 1 | 1 | +0 | 0% |
| Assault on a Police Officer | 1 | 1 | +0 | 0% |
| Offenses Against Family & Children | 6 | 6 | +0 | 0% |
| Weapon Violations | 6 | 6 | +0 | 0% |
| Simple Assault | 66 | 55 | -11 | -17% |
| Damage to Property | 9 | 6 | -3 | -33% |
| Other Crimes | 14 | 8 | -6 | -43% |
| Burglary | 2 | 1 | -1 | -50% |
| Assault with a Dangerous Weapon | 2 | 0 | -2 | -100% |
| Robbery | 1 | 0 | -1 | -100% |
| Sex Abuse | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 1 | +1 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Offenses | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_406_categories.png)

\newpage
## PSA 407

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 15 | 41 | +26 | +173% |
| Assault on a Police Officer | 1 | 2 | +1 | +100% |
| Sex Offenses | 1 | 2 | +1 | +100% |
| Weapon Violations | 7 | 10 | +3 | +43% |
| Simple Assault | 43 | 58 | +15 | +35% |
| Property Crimes | 3 | 4 | +1 | +33% |
| Theft | 3 | 4 | +1 | +33% |
| Other Crimes | 7 | 9 | +2 | +29% |
| Assault with a Dangerous Weapon | 4 | 4 | +0 | 0% |
| Driving/Boating While Intoxicated | 13 | 12 | -1 | -8% |
| Release Violations/Fugitive | 15 | 10 | -5 | -33% |
| Narcotics | 4 | 2 | -2 | -50% |
| Offenses Against Family & Children | 5 | 2 | -3 | -60% |
| Damage to Property | 9 | 3 | -6 | -67% |
| Burglary | 1 | 0 | -1 | -100% |
| Homicide | 2 | 0 | -2 | -100% |
| Aggravated Assault | 0 | 1 | +1 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Liquor Law Violations | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Robbery | 0 | 2 | +2 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_407_categories.png)

\newpage
## PSA 408

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 1 | 7 | +6 | +600% |
| Offenses Against Family & Children | 1 | 4 | +3 | +300% |
| Robbery | 2 | 6 | +4 | +200% |
| Narcotics | 4 | 9 | +5 | +125% |
| Theft | 6 | 11 | +5 | +83% |
| Property Crimes | 5 | 7 | +2 | +40% |
| Release Violations/Fugitive | 23 | 31 | +8 | +35% |
| Simple Assault | 43 | 48 | +5 | +12% |
| Driving/Boating While Intoxicated | 5 | 5 | +0 | 0% |
| Theft from Auto | 1 | 1 | +0 | 0% |
| Weapon Violations | 4 | 4 | +0 | 0% |
| Traffic Violations | 16 | 13 | -3 | -19% |
| Assault with a Dangerous Weapon | 4 | 3 | -1 | -25% |
| Damage to Property | 6 | 4 | -2 | -33% |
| Other Crimes | 15 | 6 | -9 | -60% |
| Assault on a Police Officer | 2 | 0 | -2 | -100% |
| Sex Offenses | 2 | 0 | -2 | -100% |
| Aggravated Assault | 0 | 2 | +2 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Burglary | 0 | 5 | +5 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 1 | +1 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_408_categories.png)

\newpage
## PSA 409

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 6 | 12 | +6 | +100% |
| Theft | 8 | 16 | +8 | +100% |
| Traffic Violations | 13 | 24 | +11 | +85% |
| Release Violations/Fugitive | 16 | 25 | +9 | +56% |
| Simple Assault | 39 | 52 | +13 | +33% |
| Driving/Boating While Intoxicated | 7 | 9 | +2 | +29% |
| Weapon Violations | 8 | 10 | +2 | +25% |
| Damage to Property | 7 | 6 | -1 | -14% |
| Assault with a Dangerous Weapon | 3 | 2 | -1 | -33% |
| Robbery | 3 | 2 | -1 | -33% |
| Assault on a Police Officer | 2 | 1 | -1 | -50% |
| Burglary | 2 | 1 | -1 | -50% |
| Sex Offenses | 2 | 1 | -1 | -50% |
| Other Crimes | 20 | 7 | -13 | -65% |
| Property Crimes | 7 | 1 | -6 | -86% |
| Aggravated Assault | 1 | 0 | -1 | -100% |
| Liquor Law Violations | 1 | 0 | -1 | -100% |
| Offenses Against Family & Children | 7 | 0 | -7 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 2 | +2 | N/A |
| Fraud and Financial Crimes | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 2 | +2 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_409_categories.png)

\newpage
## PSA 501

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Aggravated Assault | 1 | 4 | +3 | +300% |
| Traffic Violations | 10 | 33 | +23 | +230% |
| Motor Vehicle Theft | 1 | 3 | +2 | +200% |
| Burglary | 1 | 2 | +1 | +100% |
| Offenses Against Family & Children | 3 | 4 | +1 | +33% |
| Weapon Violations | 17 | 21 | +4 | +24% |
| Fraud and Financial Crimes | 1 | 1 | +0 | 0% |
| Homicide | 2 | 2 | +0 | 0% |
| Liquor Law Violations | 2 | 2 | +0 | 0% |
| Narcotics | 9 | 9 | +0 | 0% |
| Release Violations/Fugitive | 20 | 20 | +0 | 0% |
| Robbery | 4 | 4 | +0 | 0% |
| Damage to Property | 16 | 15 | -1 | -6% |
| Theft | 24 | 22 | -2 | -8% |
| Property Crimes | 9 | 8 | -1 | -11% |
| Assault on a Police Officer | 14 | 11 | -3 | -21% |
| Simple Assault | 119 | 93 | -26 | -22% |
| Other Crimes | 34 | 23 | -11 | -32% |
| Disorderly Conduct | 3 | 2 | -1 | -33% |
| Driving/Boating While Intoxicated | 17 | 10 | -7 | -41% |
| Assault with a Dangerous Weapon | 7 | 3 | -4 | -57% |
| Sex Offenses | 4 | 1 | -3 | -75% |
| Kidnapping | 2 | 0 | -2 | -100% |
| Sex Abuse | 1 | 0 | -1 | -100% |
| Theft from Auto | 2 | 0 | -2 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_501_categories.png)

\newpage
## PSA 502

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Aggravated Assault | 1 | 9 | +8 | +800% |
| Robbery | 1 | 7 | +6 | +600% |
| Traffic Violations | 5 | 16 | +11 | +220% |
| Liquor Law Violations | 2 | 5 | +3 | +150% |
| Release Violations/Fugitive | 11 | 27 | +16 | +145% |
| Theft | 7 | 15 | +8 | +114% |
| Assault on a Police Officer | 2 | 3 | +1 | +50% |
| Property Crimes | 8 | 11 | +3 | +38% |
| Driving/Boating While Intoxicated | 10 | 13 | +3 | +30% |
| Weapon Violations | 22 | 23 | +1 | +5% |
| Assault with a Dangerous Weapon | 10 | 10 | +0 | 0% |
| Offenses Against Family & Children | 8 | 7 | -1 | -12% |
| Other Crimes | 13 | 11 | -2 | -15% |
| Simple Assault | 122 | 101 | -21 | -17% |
| Damage to Property | 18 | 14 | -4 | -22% |
| Narcotics | 11 | 6 | -5 | -45% |
| Burglary | 2 | 0 | -2 | -100% |
| Homicide | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 3 | +3 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 1 | +1 | N/A |
| Sex Offenses | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_502_categories.png)

\newpage
## PSA 503

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 1 | 7 | +6 | +600% |
| Theft | 3 | 12 | +9 | +300% |
| Sex Offenses | 2 | 7 | +5 | +250% |
| Aggravated Assault | 2 | 6 | +4 | +200% |
| Driving/Boating While Intoxicated | 9 | 24 | +15 | +167% |
| Narcotics | 5 | 13 | +8 | +160% |
| Traffic Violations | 41 | 82 | +41 | +100% |
| Offenses Against Family & Children | 5 | 8 | +3 | +60% |
| Fraud and Financial Crimes | 2 | 3 | +1 | +50% |
| Assault on a Police Officer | 5 | 6 | +1 | +20% |
| Robbery | 6 | 7 | +1 | +17% |
| Release Violations/Fugitive | 24 | 27 | +3 | +12% |
| Other Crimes | 27 | 29 | +2 | +7% |
| Burglary | 3 | 3 | +0 | 0% |
| Damage to Property | 13 | 12 | -1 | -8% |
| Property Crimes | 8 | 7 | -1 | -12% |
| Simple Assault | 109 | 92 | -17 | -16% |
| Weapon Violations | 16 | 10 | -6 | -38% |
| Assault with a Dangerous Weapon | 7 | 4 | -3 | -43% |
| Disorderly Conduct | 9 | 0 | -9 | -100% |
| Homicide | 1 | 0 | -1 | -100% |
| Motor Vehicle Theft | 1 | 0 | -1 | -100% |
| Sex Abuse | 2 | 0 | -2 | -100% |
| Vending Violations | 1 | 0 | -1 | -100% |
| Arson | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |

![](images/psa_503_categories.png)

\newpage
## PSA 504

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Offenses Against Family & Children | 1 | 3 | +2 | +200% |
| Robbery | 3 | 5 | +2 | +67% |
| Theft | 5 | 8 | +3 | +60% |
| Damage to Property | 6 | 9 | +3 | +50% |
| Simple Assault | 29 | 31 | +2 | +7% |
| Release Violations/Fugitive | 38 | 39 | +1 | +3% |
| Traffic Violations | 11 | 8 | -3 | -27% |
| Narcotics | 5 | 3 | -2 | -40% |
| Assault on a Police Officer | 4 | 2 | -2 | -50% |
| Burglary | 2 | 1 | -1 | -50% |
| Liquor Law Violations | 2 | 1 | -1 | -50% |
| Weapon Violations | 9 | 4 | -5 | -56% |
| Driving/Boating While Intoxicated | 12 | 3 | -9 | -75% |
| Other Crimes | 4 | 1 | -3 | -75% |
| Assault with a Dangerous Weapon | 6 | 1 | -5 | -83% |
| Sex Offenses | 2 | 0 | -2 | -100% |
| Aggravated Assault | 0 | 2 | +2 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Property Crimes | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_504_categories.png)

\newpage
## PSA 505

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 5 | 13 | +8 | +160% |
| Aggravated Assault | 2 | 4 | +2 | +100% |
| Traffic Violations | 13 | 24 | +11 | +85% |
| Property Crimes | 7 | 11 | +4 | +57% |
| Liquor Law Violations | 3 | 4 | +1 | +33% |
| Damage to Property | 11 | 10 | -1 | -9% |
| Assault with a Dangerous Weapon | 8 | 6 | -2 | -25% |
| Simple Assault | 95 | 67 | -28 | -29% |
| Driving/Boating While Intoxicated | 16 | 10 | -6 | -38% |
| Release Violations/Fugitive | 21 | 11 | -10 | -48% |
| Offenses Against Family & Children | 2 | 1 | -1 | -50% |
| Robbery | 2 | 1 | -1 | -50% |
| Theft | 75 | 36 | -39 | -52% |
| Assault on a Police Officer | 9 | 4 | -5 | -56% |
| Weapon Violations | 27 | 12 | -15 | -56% |
| Other Crimes | 61 | 10 | -51 | -84% |
| Burglary | 4 | 0 | -4 | -100% |
| Disorderly Conduct | 1 | 0 | -1 | -100% |
| Sex Abuse | 1 | 0 | -1 | -100% |
| Sex Offenses | 3 | 0 | -3 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 1 | +1 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_505_categories.png)

\newpage
## PSA 506

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 4 | 63 | +59 | +1475% |
| Theft from Auto | 1 | 4 | +3 | +300% |
| Narcotics | 17 | 60 | +43 | +253% |
| Aggravated Assault | 4 | 13 | +9 | +225% |
| Homicide | 1 | 3 | +2 | +200% |
| Traffic Violations | 42 | 99 | +57 | +136% |
| Disorderly Conduct | 3 | 6 | +3 | +100% |
| Motor Vehicle Theft | 1 | 2 | +1 | +100% |
| Assault with a Dangerous Weapon | 8 | 13 | +5 | +62% |
| Theft | 26 | 36 | +10 | +38% |
| Release Violations/Fugitive | 51 | 58 | +7 | +14% |
| Robbery | 5 | 5 | +0 | 0% |
| Sex Offenses | 2 | 2 | +0 | 0% |
| Simple Assault | 126 | 122 | -4 | -3% |
| Burglary | 8 | 7 | -1 | -12% |
| Other Crimes | 16 | 14 | -2 | -12% |
| Weapon Violations | 33 | 28 | -5 | -15% |
| Assault on a Police Officer | 9 | 7 | -2 | -22% |
| Offenses Against Family & Children | 11 | 8 | -3 | -27% |
| Property Crimes | 14 | 9 | -5 | -36% |
| Driving/Boating While Intoxicated | 11 | 6 | -5 | -45% |
| Damage to Property | 14 | 7 | -7 | -50% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_506_categories.png)

\newpage
## PSA 507

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 5 | 43 | +38 | +760% |
| Homicide | 1 | 4 | +3 | +300% |
| Theft | 34 | 132 | +98 | +288% |
| Traffic Violations | 28 | 96 | +68 | +243% |
| Narcotics | 29 | 84 | +55 | +190% |
| Assault with a Dangerous Weapon | 13 | 22 | +9 | +69% |
| Driving/Boating While Intoxicated | 12 | 20 | +8 | +67% |
| Burglary | 4 | 6 | +2 | +50% |
| Offenses Against Family & Children | 10 | 13 | +3 | +30% |
| Aggravated Assault | 7 | 9 | +2 | +29% |
| Other Crimes | 29 | 34 | +5 | +17% |
| Robbery | 9 | 9 | +0 | 0% |
| Weapon Violations | 65 | 59 | -6 | -9% |
| Release Violations/Fugitive | 57 | 48 | -9 | -16% |
| Property Crimes | 25 | 20 | -5 | -20% |
| Simple Assault | 230 | 180 | -50 | -22% |
| Motor Vehicle Theft | 4 | 3 | -1 | -25% |
| Sex Offenses | 4 | 3 | -1 | -25% |
| Damage to Property | 28 | 17 | -11 | -39% |
| Assault on a Police Officer | 13 | 7 | -6 | -46% |
| Kidnapping | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 6 | +6 | N/A |
| Fraud and Financial Crimes | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_507_categories.png)

\newpage
## PSA 601

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 2 | 10 | +8 | +400% |
| Traffic Violations | 5 | 21 | +16 | +320% |
| Aggravated Assault | 1 | 3 | +2 | +200% |
| Assault on a Police Officer | 1 | 2 | +1 | +100% |
| Liquor Law Violations | 1 | 2 | +1 | +100% |
| Assault with a Dangerous Weapon | 2 | 2 | +0 | 0% |
| Theft | 1 | 1 | +0 | 0% |
| Driving/Boating While Intoxicated | 4 | 3 | -1 | -25% |
| Simple Assault | 57 | 35 | -22 | -39% |
| Offenses Against Family & Children | 4 | 2 | -2 | -50% |
| Property Crimes | 2 | 1 | -1 | -50% |
| Release Violations/Fugitive | 14 | 7 | -7 | -50% |
| Weapon Violations | 23 | 11 | -12 | -52% |
| Other Crimes | 14 | 5 | -9 | -64% |
| Damage to Property | 9 | 3 | -6 | -67% |
| Sex Offenses | 3 | 1 | -2 | -67% |
| Homicide | 2 | 0 | -2 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Burglary | 0 | 2 | +2 | N/A |
| Disorderly Conduct | 0 | 2 | +2 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Robbery | 0 | 3 | +3 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_601_categories.png)

\newpage
## PSA 602

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 24 | 474 | +450 | +1875% |
| Liquor Law Violations | 4 | 33 | +29 | +725% |
| Burglary | 2 | 7 | +5 | +250% |
| Sex Offenses | 1 | 2 | +1 | +100% |
| Offenses Against Family & Children | 7 | 13 | +6 | +86% |
| Assault with a Dangerous Weapon | 6 | 11 | +5 | +83% |
| Narcotics | 10 | 16 | +6 | +60% |
| Theft | 8 | 12 | +4 | +50% |
| Release Violations/Fugitive | 29 | 42 | +13 | +45% |
| Other Crimes | 12 | 13 | +1 | +8% |
| Homicide | 2 | 2 | +0 | 0% |
| Simple Assault | 140 | 134 | -6 | -4% |
| Property Crimes | 22 | 21 | -1 | -5% |
| Damage to Property | 17 | 16 | -1 | -6% |
| Robbery | 4 | 3 | -1 | -25% |
| Weapon Violations | 60 | 41 | -19 | -32% |
| Assault on a Police Officer | 5 | 3 | -2 | -40% |
| Driving/Boating While Intoxicated | 15 | 8 | -7 | -47% |
| Aggravated Assault | 4 | 2 | -2 | -50% |
| Disorderly Conduct | 1 | 0 | -1 | -100% |
| Prostitution | 4 | 0 | -4 | -100% |
| Sex Abuse | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 2 | +2 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_602_categories.png)

\newpage
## PSA 603

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 16 | 237 | +221 | +1381% |
| Theft | 6 | 41 | +35 | +583% |
| Liquor Law Violations | 8 | 49 | +41 | +512% |
| Burglary | 1 | 4 | +3 | +300% |
| Sex Offenses | 1 | 4 | +3 | +300% |
| Aggravated Assault | 1 | 3 | +2 | +200% |
| Fraud and Financial Crimes | 1 | 2 | +1 | +100% |
| Narcotics | 22 | 41 | +19 | +86% |
| Offenses Against Family & Children | 8 | 9 | +1 | +12% |
| Assault on a Police Officer | 6 | 6 | +0 | 0% |
| Homicide | 2 | 2 | +0 | 0% |
| Sex Abuse | 1 | 1 | +0 | 0% |
| Damage to Property | 23 | 20 | -3 | -13% |
| Assault with a Dangerous Weapon | 22 | 19 | -3 | -14% |
| Other Crimes | 27 | 22 | -5 | -19% |
| Simple Assault | 187 | 145 | -42 | -22% |
| Driving/Boating While Intoxicated | 13 | 10 | -3 | -23% |
| Robbery | 10 | 7 | -3 | -30% |
| Property Crimes | 38 | 25 | -13 | -34% |
| Release Violations/Fugitive | 53 | 33 | -20 | -38% |
| Weapon Violations | 85 | 51 | -34 | -40% |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_603_categories.png)

\newpage
## PSA 604

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Traffic Violations | 8 | 127 | +119 | +1488% |
| Liquor Law Violations | 3 | 45 | +42 | +1400% |
| Theft | 3 | 8 | +5 | +167% |
| Offenses Against Family & Children | 6 | 13 | +7 | +117% |
| Homicide | 1 | 2 | +1 | +100% |
| Narcotics | 20 | 30 | +10 | +50% |
| Assault on a Police Officer | 3 | 4 | +1 | +33% |
| Burglary | 3 | 4 | +1 | +33% |
| Assault with a Dangerous Weapon | 9 | 10 | +1 | +11% |
| Damage to Property | 18 | 20 | +2 | +11% |
| Property Crimes | 15 | 16 | +1 | +7% |
| Simple Assault | 162 | 163 | +1 | +1% |
| Release Violations/Fugitive | 45 | 32 | -13 | -29% |
| Weapon Violations | 75 | 47 | -28 | -37% |
| Driving/Boating While Intoxicated | 12 | 7 | -5 | -42% |
| Motor Vehicle Theft | 2 | 1 | -1 | -50% |
| Robbery | 8 | 3 | -5 | -62% |
| Sex Abuse | 3 | 1 | -2 | -67% |
| Other Crimes | 21 | 6 | -15 | -71% |
| Sex Offenses | 5 | 0 | -5 | -100% |
| Aggravated Assault | 0 | 7 | +7 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 2 | +2 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 3 | +3 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_604_categories.png)

\newpage
## PSA 605

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 1 | 17 | +16 | +1600% |
| Theft | 1 | 7 | +6 | +600% |
| Traffic Violations | 5 | 30 | +25 | +500% |
| Property Crimes | 7 | 11 | +4 | +57% |
| Driving/Boating While Intoxicated | 4 | 5 | +1 | +25% |
| Weapon Violations | 24 | 28 | +4 | +17% |
| Release Violations/Fugitive | 10 | 11 | +1 | +10% |
| Aggravated Assault | 2 | 2 | +0 | 0% |
| Other Crimes | 7 | 7 | +0 | 0% |
| Simple Assault | 69 | 60 | -9 | -13% |
| Damage to Property | 7 | 6 | -1 | -14% |
| Offenses Against Family & Children | 4 | 3 | -1 | -25% |
| Assault with a Dangerous Weapon | 2 | 1 | -1 | -50% |
| Assault on a Police Officer | 2 | 0 | -2 | -100% |
| Homicide | 1 | 0 | -1 | -100% |
| Kidnapping | 1 | 0 | -1 | -100% |
| Sex Abuse | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Burglary | 0 | 2 | +2 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Narcotics | 0 | 4 | +4 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Robbery | 0 | 2 | +2 | N/A |
| Sex Offenses | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_605_categories.png)

\newpage
## PSA 606

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 2 | 7 | +5 | +250% |
| Weapon Violations | 4 | 11 | +7 | +175% |
| Theft | 9 | 21 | +12 | +133% |
| Aggravated Assault | 2 | 4 | +2 | +100% |
| Assault on a Police Officer | 4 | 8 | +4 | +100% |
| Traffic Violations | 9 | 16 | +7 | +78% |
| Property Crimes | 9 | 12 | +3 | +33% |
| Simple Assault | 44 | 57 | +13 | +30% |
| Assault with a Dangerous Weapon | 4 | 5 | +1 | +25% |
| Release Violations/Fugitive | 10 | 12 | +2 | +20% |
| Liquor Law Violations | 1 | 1 | +0 | 0% |
| Other Crimes | 13 | 10 | -3 | -23% |
| Offenses Against Family & Children | 3 | 2 | -1 | -33% |
| Damage to Property | 9 | 4 | -5 | -56% |
| Driving/Boating While Intoxicated | 8 | 3 | -5 | -62% |
| Kidnapping | 1 | 0 | -1 | -100% |
| Robbery | 1 | 0 | -1 | -100% |
| Sex Offenses | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Burglary | 0 | 1 | +1 | N/A |
| Disorderly Conduct | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_606_categories.png)

\newpage
## PSA 607

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 1 | 51 | +50 | +5000% |
| Narcotics | 13 | 43 | +30 | +231% |
| Traffic Violations | 13 | 37 | +24 | +185% |
| Theft | 3 | 7 | +4 | +133% |
| Disorderly Conduct | 1 | 2 | +1 | +100% |
| Assault with a Dangerous Weapon | 9 | 14 | +5 | +56% |
| Burglary | 4 | 5 | +1 | +25% |
| Homicide | 4 | 5 | +1 | +25% |
| Damage to Property | 14 | 17 | +3 | +21% |
| Simple Assault | 110 | 112 | +2 | +2% |
| Aggravated Assault | 5 | 5 | +0 | 0% |
| Weapon Violations | 53 | 51 | -2 | -4% |
| Other Crimes | 18 | 16 | -2 | -11% |
| Property Crimes | 18 | 15 | -3 | -17% |
| Release Violations/Fugitive | 44 | 36 | -8 | -18% |
| Offenses Against Family & Children | 12 | 6 | -6 | -50% |
| Robbery | 2 | 1 | -1 | -50% |
| Assault on a Police Officer | 5 | 2 | -3 | -60% |
| Driving/Boating While Intoxicated | 10 | 3 | -7 | -70% |
| Prostitution | 5 | 0 | -5 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Sex Abuse | 0 | 1 | +1 | N/A |
| Sex Offenses | 0 | 3 | +3 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_607_categories.png)

\newpage
## PSA 608

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 4 | 71 | +67 | +1675% |
| Traffic Violations | 13 | 170 | +157 | +1208% |
| Sex Offenses | 4 | 10 | +6 | +150% |
| Disorderly Conduct | 2 | 4 | +2 | +100% |
| Narcotics | 18 | 26 | +8 | +44% |
| Offenses Against Family & Children | 11 | 15 | +4 | +36% |
| Robbery | 9 | 11 | +2 | +22% |
| Release Violations/Fugitive | 42 | 51 | +9 | +21% |
| Property Crimes | 10 | 12 | +2 | +20% |
| Assault on a Police Officer | 7 | 8 | +1 | +14% |
| Assault with a Dangerous Weapon | 12 | 13 | +1 | +8% |
| Driving/Boating While Intoxicated | 2 | 2 | +0 | 0% |
| Homicide | 1 | 1 | +0 | 0% |
| Theft | 3 | 3 | +0 | 0% |
| Simple Assault | 123 | 117 | -6 | -5% |
| Damage to Property | 17 | 13 | -4 | -24% |
| Other Crimes | 19 | 14 | -5 | -26% |
| Weapon Violations | 42 | 24 | -18 | -43% |
| Aggravated Assault | 2 | 1 | -1 | -50% |
| Burglary | 2 | 1 | -1 | -50% |
| Sex Abuse | 2 | 1 | -1 | -50% |
| Kidnapping | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 2 | +2 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_608_categories.png)

\newpage
## PSA 701

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 2 | 27 | +25 | +1250% |
| Aggravated Assault | 1 | 7 | +6 | +600% |
| Narcotics | 8 | 45 | +37 | +462% |
| Traffic Violations | 10 | 47 | +37 | +370% |
| Theft | 2 | 9 | +7 | +350% |
| Property Crimes | 6 | 16 | +10 | +167% |
| Burglary | 1 | 2 | +1 | +100% |
| Assault on a Police Officer | 5 | 7 | +2 | +40% |
| Weapon Violations | 33 | 40 | +7 | +21% |
| Damage to Property | 10 | 12 | +2 | +20% |
| Offenses Against Family & Children | 8 | 8 | +0 | 0% |
| Sex Offenses | 4 | 3 | -1 | -25% |
| Simple Assault | 131 | 93 | -38 | -29% |
| Other Crimes | 11 | 7 | -4 | -36% |
| Assault with a Dangerous Weapon | 7 | 4 | -3 | -43% |
| Release Violations/Fugitive | 30 | 17 | -13 | -43% |
| Driving/Boating While Intoxicated | 16 | 9 | -7 | -44% |
| Robbery | 5 | 2 | -3 | -60% |
| Homicide | 1 | 0 | -1 | -100% |
| Sex Abuse | 1 | 0 | -1 | -100% |
| Arson | 0 | 1 | +1 | N/A |
| Disorderly Conduct | 0 | 2 | +2 | N/A |
| Fraud and Financial Crimes | 0 | 2 | +2 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 1 | +1 | N/A |
| Motor Vehicle Theft | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_701_categories.png)

\newpage
## PSA 702

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 8 | 51 | +43 | +538% |
| Disorderly Conduct | 2 | 8 | +6 | +300% |
| Motor Vehicle Theft | 1 | 4 | +3 | +300% |
| Burglary | 2 | 7 | +5 | +250% |
| Sex Abuse | 1 | 3 | +2 | +200% |
| Assault with a Dangerous Weapon | 10 | 23 | +13 | +130% |
| Aggravated Assault | 5 | 11 | +6 | +120% |
| Theft | 5 | 11 | +6 | +120% |
| Assault on a Police Officer | 6 | 12 | +6 | +100% |
| Weapon Violations | 34 | 64 | +30 | +88% |
| Other Crimes | 15 | 27 | +12 | +80% |
| Traffic Violations | 26 | 38 | +12 | +46% |
| Robbery | 5 | 6 | +1 | +20% |
| Release Violations/Fugitive | 49 | 53 | +4 | +8% |
| Simple Assault | 172 | 176 | +4 | +2% |
| Damage to Property | 17 | 17 | +0 | 0% |
| Homicide | 3 | 3 | +0 | 0% |
| Property Crimes | 18 | 17 | -1 | -6% |
| Driving/Boating While Intoxicated | 7 | 6 | -1 | -14% |
| Offenses Against Family & Children | 16 | 10 | -6 | -38% |
| Sex Offenses | 6 | 3 | -3 | -50% |
| Kidnapping | 3 | 1 | -2 | -67% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 2 | +2 | N/A |
| Liquor Law Violations | 0 | 9 | +9 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_702_categories.png)

\newpage
## PSA 703

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 4 | 50 | +46 | +1150% |
| Traffic Violations | 14 | 72 | +58 | +414% |
| Aggravated Assault | 2 | 7 | +5 | +250% |
| Sex Offenses | 2 | 5 | +3 | +150% |
| Theft | 6 | 11 | +5 | +83% |
| Other Crimes | 10 | 18 | +8 | +80% |
| Assault with a Dangerous Weapon | 8 | 10 | +2 | +25% |
| Weapon Violations | 44 | 55 | +11 | +25% |
| Damage to Property | 15 | 18 | +3 | +20% |
| Driving/Boating While Intoxicated | 22 | 25 | +3 | +14% |
| Simple Assault | 148 | 154 | +6 | +4% |
| Release Violations/Fugitive | 34 | 28 | -6 | -18% |
| Assault on a Police Officer | 20 | 16 | -4 | -20% |
| Offenses Against Family & Children | 13 | 9 | -4 | -31% |
| Property Crimes | 12 | 7 | -5 | -42% |
| Homicide | 2 | 1 | -1 | -50% |
| Robbery | 9 | 4 | -5 | -56% |
| Sex Abuse | 2 | 0 | -2 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Burglary | 0 | 6 | +6 | N/A |
| Disorderly Conduct | 0 | 4 | +4 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 2 | +2 | N/A |
| Liquor Law Violations | 0 | 25 | +25 | N/A |
| Motor Vehicle Theft | 0 | 3 | +3 | N/A |
| Prostitution | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_703_categories.png)

\newpage
## PSA 704

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Burglary | 1 | 10 | +9 | +900% |
| Disorderly Conduct | 1 | 7 | +6 | +600% |
| Narcotics | 7 | 48 | +41 | +586% |
| Liquor Law Violations | 4 | 24 | +20 | +500% |
| Robbery | 1 | 5 | +4 | +400% |
| Traffic Violations | 14 | 60 | +46 | +329% |
| Release Violations/Fugitive | 30 | 38 | +8 | +27% |
| Other Crimes | 34 | 43 | +9 | +26% |
| Property Crimes | 16 | 19 | +3 | +19% |
| Assault on a Police Officer | 13 | 15 | +2 | +15% |
| Weapon Violations | 54 | 62 | +8 | +15% |
| Aggravated Assault | 7 | 8 | +1 | +14% |
| Damage to Property | 15 | 16 | +1 | +7% |
| Theft | 15 | 16 | +1 | +7% |
| Driving/Boating While Intoxicated | 17 | 17 | +0 | 0% |
| Homicide | 1 | 1 | +0 | 0% |
| Sex Abuse | 1 | 1 | +0 | 0% |
| Sex Offenses | 1 | 1 | +0 | 0% |
| Offenses Against Family & Children | 15 | 13 | -2 | -13% |
| Simple Assault | 177 | 134 | -43 | -24% |
| Assault with a Dangerous Weapon | 14 | 9 | -5 | -36% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 2 | +2 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_704_categories.png)

\newpage
## PSA 705

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 1 | 8 | +7 | +700% |
| Traffic Violations | 9 | 61 | +52 | +578% |
| Assault on a Police Officer | 2 | 10 | +8 | +400% |
| Narcotics | 6 | 29 | +23 | +383% |
| Aggravated Assault | 1 | 4 | +3 | +300% |
| Weapon Violations | 12 | 38 | +26 | +217% |
| Burglary | 1 | 2 | +1 | +100% |
| Offenses Against Family & Children | 3 | 5 | +2 | +67% |
| Property Crimes | 6 | 10 | +4 | +67% |
| Release Violations/Fugitive | 10 | 15 | +5 | +50% |
| Theft | 3 | 4 | +1 | +33% |
| Sex Abuse | 2 | 2 | +0 | 0% |
| Simple Assault | 94 | 91 | -3 | -3% |
| Driving/Boating While Intoxicated | 14 | 11 | -3 | -21% |
| Assault with a Dangerous Weapon | 5 | 3 | -2 | -40% |
| Other Crimes | 10 | 5 | -5 | -50% |
| Damage to Property | 13 | 6 | -7 | -54% |
| Arson | 1 | 0 | -1 | -100% |
| Sex Offenses | 3 | 0 | -3 | -100% |
| Disorderly Conduct | 0 | 1 | +1 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 2 | +2 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Robbery | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_705_categories.png)

\newpage
## PSA 706

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 1 | 11 | +10 | +1000% |
| Disorderly Conduct | 1 | 5 | +4 | +400% |
| Sex Offenses | 1 | 5 | +4 | +400% |
| Traffic Violations | 9 | 41 | +32 | +356% |
| Narcotics | 11 | 42 | +31 | +282% |
| Aggravated Assault | 4 | 13 | +9 | +225% |
| Other Crimes | 24 | 49 | +25 | +104% |
| Motor Vehicle Theft | 1 | 2 | +1 | +100% |
| Release Violations/Fugitive | 26 | 37 | +11 | +42% |
| Offenses Against Family & Children | 8 | 11 | +3 | +38% |
| Property Crimes | 15 | 19 | +4 | +27% |
| Assault with a Dangerous Weapon | 13 | 15 | +2 | +15% |
| Weapon Violations | 35 | 39 | +4 | +11% |
| Assault on a Police Officer | 14 | 15 | +1 | +7% |
| Simple Assault | 121 | 128 | +7 | +6% |
| Burglary | 1 | 1 | +0 | 0% |
| Homicide | 2 | 2 | +0 | 0% |
| Theft | 6 | 6 | +0 | 0% |
| Damage to Property | 14 | 10 | -4 | -29% |
| Driving/Boating While Intoxicated | 11 | 7 | -4 | -36% |
| Sex Abuse | 3 | 1 | -2 | -67% |
| Kidnapping | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 8 | +8 | N/A |
| Robbery | 0 | 1 | +1 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_706_categories.png)

\newpage
## PSA 707

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 1 | 26 | +25 | +2500% |
| Narcotics | 15 | 62 | +47 | +313% |
| Disorderly Conduct | 1 | 4 | +3 | +300% |
| Aggravated Assault | 3 | 10 | +7 | +233% |
| Property Crimes | 7 | 23 | +16 | +229% |
| Theft | 3 | 9 | +6 | +200% |
| Traffic Violations | 16 | 42 | +26 | +162% |
| Sex Offenses | 1 | 2 | +1 | +100% |
| Assault on a Police Officer | 6 | 8 | +2 | +33% |
| Simple Assault | 108 | 130 | +22 | +20% |
| Assault with a Dangerous Weapon | 12 | 14 | +2 | +17% |
| Robbery | 1 | 1 | +0 | 0% |
| Release Violations/Fugitive | 44 | 40 | -4 | -9% |
| Other Crimes | 16 | 13 | -3 | -19% |
| Offenses Against Family & Children | 13 | 10 | -3 | -23% |
| Weapon Violations | 42 | 27 | -15 | -36% |
| Driving/Boating While Intoxicated | 24 | 13 | -11 | -46% |
| Damage to Property | 23 | 9 | -14 | -61% |
| Sex Abuse | 2 | 0 | -2 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Burglary | 0 | 1 | +1 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 2 | +2 | N/A |
| Kidnapping | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 0 | +0 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_707_categories.png)

\newpage
## PSA 708

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Liquor Law Violations | 3 | 11 | +8 | +267% |
| Traffic Violations | 20 | 62 | +42 | +210% |
| Theft | 4 | 12 | +8 | +200% |
| Aggravated Assault | 4 | 10 | +6 | +150% |
| Sex Abuse | 1 | 2 | +1 | +100% |
| Assault with a Dangerous Weapon | 11 | 18 | +7 | +64% |
| Assault on a Police Officer | 7 | 11 | +4 | +57% |
| Other Crimes | 33 | 49 | +16 | +48% |
| Driving/Boating While Intoxicated | 20 | 26 | +6 | +30% |
| Narcotics | 64 | 73 | +9 | +14% |
| Damage to Property | 18 | 19 | +1 | +6% |
| Burglary | 2 | 2 | +0 | 0% |
| Property Crimes | 19 | 16 | -3 | -16% |
| Offenses Against Family & Children | 20 | 16 | -4 | -20% |
| Robbery | 6 | 4 | -2 | -33% |
| Simple Assault | 202 | 134 | -68 | -34% |
| Weapon Violations | 56 | 34 | -22 | -39% |
| Release Violations/Fugitive | 38 | 22 | -16 | -42% |
| Disorderly Conduct | 4 | 2 | -2 | -50% |
| Homicide | 4 | 1 | -3 | -75% |
| Kidnapping | 1 | 0 | -1 | -100% |
| Motor Vehicle Theft | 2 | 0 | -2 | -100% |
| Sex Offenses | 3 | 0 | -3 | -100% |
| Theft from Auto | 1 | 0 | -1 | -100% |
| Arson | 0 | 0 | +0 | N/A |
| Fraud and Financial Crimes | 0 | 0 | +0 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Prostitution | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_708_categories.png)

\newpage
## PSA Unknown

| Arrest Category | 2023 | 2024 | Change | % Change |
|----------------|------:|------:|--------:|----------:|
| Narcotics | 5 | 36 | +31 | +620% |
| Damage to Property | 1 | 6 | +5 | +500% |
| Liquor Law Violations | 6 | 36 | +30 | +500% |
| Traffic Violations | 14 | 83 | +69 | +493% |
| Release Violations/Fugitive | 4 | 17 | +13 | +325% |
| Assault on a Police Officer | 2 | 8 | +6 | +300% |
| Driving/Boating While Intoxicated | 18 | 50 | +32 | +178% |
| Theft | 5 | 13 | +8 | +160% |
| Simple Assault | 18 | 42 | +24 | +133% |
| Property Crimes | 4 | 9 | +5 | +125% |
| Offenses Against Family & Children | 1 | 2 | +1 | +100% |
| Robbery | 2 | 4 | +2 | +100% |
| Weapon Violations | 14 | 25 | +11 | +79% |
| Assault with a Dangerous Weapon | 3 | 2 | -1 | -33% |
| Burglary | 1 | 0 | -1 | -100% |
| Kidnapping | 1 | 0 | -1 | -100% |
| Other Crimes | 1 | 0 | -1 | -100% |
| Aggravated Assault | 0 | 1 | +1 | N/A |
| Arson | 0 | 0 | +0 | N/A |
| Disorderly Conduct | 0 | 8 | +8 | N/A |
| Fraud and Financial Crimes | 0 | 1 | +1 | N/A |
| Gambling | 0 | 0 | +0 | N/A |
| Homicide | 0 | 0 | +0 | N/A |
| Motor Vehicle Theft | 0 | 1 | +1 | N/A |
| Prostitution | 0 | 3 | +3 | N/A |
| Sex Abuse | 0 | 0 | +0 | N/A |
| Sex Offenses | 0 | 0 | +0 | N/A |
| Theft from Auto | 0 | 1 | +1 | N/A |
| Vending Violations | 0 | 0 | +0 | N/A |

![](images/psa_Unknown_categories.png)

