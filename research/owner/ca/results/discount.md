# Contamination discount and recovery: LA County assessor roll

Method: see `discount.py` docstring. Price = assessed total value in the roll year after a Prop 13 base-year reset (a change of ownership), on commercial/industrial and vacant parcels, 2006-2025 rolls. Cases matched by the parcel polygon that contains the GeoTracker point. Coefficients are % price difference against nearby clean sales of the same use class, after lot size, building size, age, use code, sale year and 1 km cell.


Sale events after screens: 118,513 (79,208 parcels). Counts: {'control': 112725, 'closed_5p': 3302, 'open': 1484, 'closed_2_5': 391, 'closed_0_2': 334, 'later': 277}. Share with lot area: 0.87.


## M1 hedonic, all case types (n = 103,212)

| treatment   |    n |   coef |   pct | ci95_pct     |
|:------------|-----:|-------:|------:|:-------------|
| open        | 1481 |  0.053 |   5.4 | [0.8, 10.3]  |
| closed_0_2  |  332 |  0.107 |  11.3 | [2.6, 20.7]  |
| closed_2_5  |  385 |  0.113 |  11.9 | [4.1, 20.4]  |
| closed_5p   | 3290 |  0.071 |   7.4 | [3.9, 11.0]  |
| later       |  270 | -0.032 |  -3.2 | [-10.2, 4.4] |

Land value only (n = 103,212): open 10.5% [5.6, 15.6], closed_0_2 16.0% [7.2, 25.5], closed_2_5 17.2% [8.9, 26.3], closed_5p 11.7% [7.7, 15.8], later 2.8% [-4.8, 11.1]

### LUST (n = 101,337)

| treatment   |    n |   coef |   pct | ci95_pct      |
|:------------|-----:|-------:|------:|:--------------|
| open        |  929 |  0.059 |   6   | [-0.0, 12.4]  |
| closed_0_2  |  274 |  0.104 |  11   | [1.4, 21.5]   |
| closed_2_5  |  335 |  0.105 |  11.1 | [2.7, 20.2]   |
| closed_5p   | 2270 |  0.097 |  10.2 | [5.8, 14.8]   |
| later       |   75 | -0.025 |  -2.5 | [-14.5, 11.3] |

### Cleanup Program (n = 99,329)

| treatment   |    n |   coef |   pct | ci95_pct     |
|:------------|-----:|-------:|------:|:-------------|
| open        |  552 |  0.047 |   4.8 | [-1.8, 12.0] |
| closed_0_2  |   58 |  0.125 |  13.4 | [-6.1, 36.9] |
| closed_2_5  |   50 |  0.21  |  23.4 | [1.8, 49.6]  |
| closed_5p   | 1020 |  0.002 |   0.2 | [-4.4, 5.0]  |
| later       |  195 | -0.035 |  -3.4 | [-11.7, 5.7] |

## M2 repeat sales (parcel fixed effect; n = 37,732 pairs; open-then-closed pairs 224, open-then-open 356)

- treated: 6.9% [0.2, 14.2] relative to clean repeat sales over the same years
- still_open: 3.4% [-1.3, 8.2] relative to clean repeat sales over the same years

## D. Median price per sq ft of lot ($), by use class x sale period x treatment

|                           |   closed_0_2 |   closed_2_5 |   closed_5p |   control |   later |   open |
|:--------------------------|-------------:|-------------:|------------:|----------:|--------:|-------:|
| ('Commercial', '2005-10') |           82 |           85 |          81 |        83 |      66 |     75 |
| ('Commercial', '2011-15') |           76 |           80 |          81 |        76 |      61 |     68 |
| ('Commercial', '2016-20') |           96 |          137 |         133 |       109 |     125 |    105 |
| ('Commercial', '2021-25') |           97 |          189 |         145 |       142 |     126 |    153 |
| ('Industrial', '2005-10') |           58 |           34 |          49 |        50 |      46 |     42 |
| ('Industrial', '2011-15') |           39 |           29 |          46 |        48 |      48 |     42 |
| ('Industrial', '2016-20') |           52 |           85 |          71 |        76 |      83 |     65 |
| ('Industrial', '2021-25') |          111 |          147 |         123 |       117 |     101 |    118 |

Counts (all periods):

| UseCodeDescChar1   |   closed_0_2 |   closed_2_5 |   closed_5p |   control |   later |   open |
|:-------------------|-------------:|-------------:|------------:|----------:|--------:|-------:|
| Commercial         |          238 |          309 |        1921 |     66471 |     143 |   1027 |
| Industrial         |           94 |           76 |        1369 |     30983 |     127 |    454 |

## C. Rough margin per site (LA parcels with a Cleanup Fund reimbursed-to-date, n = 312)

Uplift = parcel value (at the open-case sale, else latest roll) x (exp(b_closed_0_2 - b_open) - 1), by case type from M1. Cost = Cleanup Fund reimbursed-to-date (Oct 2020 capture; excludes the owner's deductible and anything above the $1.5M cap).

| case type       |   parcels | recovery (closed 0-2y vs open)   |   median value $ |   median uplift $ |   median reimbursed $ |   uplift - cost p25 $ |   median $ |   p75 $ |   share positive |
|:----------------|----------:|:---------------------------------|-----------------:|------------------:|----------------------:|----------------------:|-----------:|--------:|-----------------:|
| Cleanup Program |         3 | 8.1%                             |          1327177 |            107664 |                194777 |               -658934 |    -438935 | -218935 |             0.33 |
| LUST            |       309 | 4.6%                             |          1301149 |             59889 |                643124 |              -1040800 |    -572566 | -122972 |             0.13 |

## Reading and caveats

- Recorded prices show no stigma discount. Commercial/industrial parcels that sold while a cleanup case was open sold for about
  the same as, or slightly more than, nearby clean parcels of the same use code, size, age and year. The recovery is small:
  sales 0-5 years after closure are about 5-6 points above open-case sales, and the repeat-sales model (same parcel sold
  while open, then after closure, against clean repeat sales over the same years) gives about +7%.
- Price is the assessor's full cash value set at the change of ownership (normally the purchase price under Prop 13), not
  the deed price; base years also reset on some non-sale transfers (entity changes, partial interests), which the
  screens only partly remove. Commercial sales of operating gas stations can carry business value in the price.
- Treatment is assigned by the parcel polygon containing the GeoTracker point; a case point on the street or a
  neighbouring parcel misassigns it, which biases coefficients towards zero.
- Only LA County, commercial/industrial use classes, 2006-2025 rolls; lot area from today's parcel layer (parcels
  since split or merged have no area and drop out of M1). San Francisco was not run.
- Margin table C uses the Cleanup Fund's reimbursed-to-date as the cleanup cost. The Fund, not the buyer, paid that
  money, so it is the social cost of the cleanup, not the buyer's cash cost; the buyer's own outlay is the deductible
  plus anything ineligible or above the cap.

