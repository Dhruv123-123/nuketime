# Contamination discount and recovery: LA County assessor roll

Method: see `discount.py` docstring. Price = assessed total value in the roll year after a Prop 13 base-year reset (a change of ownership), on commercial/industrial and vacant parcels, 2006-2025 rolls. Cases matched by the parcel polygon that contains the GeoTracker point. Coefficients are % price difference against nearby clean sales of the same use class, after lot size, building size, age, use code, sale year and 1 km cell.


Sale events after screens: 118,513 (79,208 parcels). Counts: {'control': 112725, 'closed_5p': 3302, 'open': 1484, 'closed_2_5': 391, 'closed_0_2': 334, 'later': 277}. Share with lot area: 0.87.


## M1 hedonic, all case types (n = 103,212)

| treatment   |    n |   coef |     se |   pct | ci95_pct     |
|:------------|-----:|-------:|-------:|------:|:-------------|
| open        | 1481 |  0.053 | 0.0229 |   5.4 | [0.8, 10.3]  |
| closed_0_2  |  332 |  0.107 | 0.0415 |  11.3 | [2.6, 20.7]  |
| closed_2_5  |  385 |  0.113 | 0.0372 |  11.9 | [4.1, 20.4]  |
| closed_5p   | 3290 |  0.071 | 0.0169 |   7.4 | [3.9, 11.0]  |
| later       |  270 | -0.032 | 0.0386 |  -3.2 | [-10.2, 4.4] |

Land value only (n = 103,212): open 10.5% [5.6, 15.6], closed_0_2 16.0% [7.2, 25.5], closed_2_5 17.2% [8.9, 26.3], closed_5p 11.7% [7.7, 15.8], later 2.8% [-4.8, 11.1]

### LUST (n = 101,337)

| treatment   |    n |   coef |     se |   pct | ci95_pct      |
|:------------|-----:|-------:|-------:|------:|:--------------|
| open        |  929 |  0.059 | 0.0299 |   6   | [-0.0, 12.4]  |
| closed_0_2  |  274 |  0.104 | 0.0461 |  11   | [1.4, 21.5]   |
| closed_2_5  |  335 |  0.105 | 0.0401 |  11.1 | [2.7, 20.2]   |
| closed_5p   | 2270 |  0.097 | 0.0208 |  10.2 | [5.8, 14.8]   |
| later       |   75 | -0.025 | 0.0672 |  -2.5 | [-14.5, 11.3] |

### Cleanup Program (n = 99,329)

| treatment   |    n |   coef |     se |   pct | ci95_pct     |
|:------------|-----:|-------:|-------:|------:|:-------------|
| open        |  552 |  0.047 | 0.0337 |   4.8 | [-1.8, 12.0] |
| closed_0_2  |   58 |  0.125 | 0.0963 |  13.4 | [-6.1, 36.9] |
| closed_2_5  |   50 |  0.21  | 0.0983 |  23.4 | [1.8, 49.6]  |
| closed_5p   | 1020 |  0.002 | 0.0239 |   0.2 | [-4.4, 5.0]  |
| later       |  195 | -0.035 | 0.0458 |  -3.4 | [-11.7, 5.7] |

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

## Other counties (San Francisco, Alameda) and the industrial-class pool

San Francisco: 2,595 commercial/industrial sale events 2007-2025; 1,698 of 2,924 cases matched to a parcel ({'address': 881, 'nearest<40m': 817}). Alameda: 11,559 parcels whose latest document is 2006 or later (one cross-section, price = current assessed value deflated at 2%/yr to the document year); 2,302 of 5,118 cases matched.


### San Francisco, all case types (n = 1,791)

| treatment   |   n |   coef |   pct | ci95_pct      |
|:------------|----:|-------:|------:|:--------------|
| open        |  13 |  0.194 |  21.4 | [-23.1, 91.7] |
| closed_0_2  |  10 |  0.143 |  15.3 | [-25.2, 77.9] |
| closed_2_5  |  10 | -0.039 |  -3.8 | [-46.5, 72.8] |
| closed_5p   | 168 |  0.065 |   6.7 | [-7.3, 22.8]  |
| later       |  13 |  0.093 |   9.8 | [-8.6, 31.8]  |

San Francisco, LUST (n = 1,789): open 7.3% [-29.2, 62.6] (n=12), closed_0_2 14.1% [-26.1, 76.3] (n=10), closed_2_5 -4.8% [-46.9, 70.9] (n=10), closed_5p 6.5% [-7.4, 22.5] (n=167), later 10.0% [-8.4, 32.1] (n=13)

San Francisco, median $ per lot sq ft by treatment: closed_0_2 412, closed_2_5 442, closed_5p 631, control 534, later 628, open 131

### Alameda, all case types (n = 11,556)

| treatment   |   n |   coef |   pct | ci95_pct     |
|:------------|----:|-------:|------:|:-------------|
| open        | 283 |  0.137 |  14.6 | [-0.3, 31.7] |
| closed_0_2  |  62 |  0.276 |  31.7 | [9.5, 58.4]  |
| closed_2_5  |  58 |  0.372 |  45.1 | [19.4, 76.2] |
| closed_5p   | 703 |  0.174 |  19   | [11.2, 27.3] |
| later       |  61 |  0.255 |  29   | [-3.5, 72.4] |

Alameda, LUST (n = 11,213): open -0.1% [-15.5, 18.1] (n=123), closed_0_2 26.0% [1.5, 56.5] (n=45), closed_2_5 50.1% [20.8, 86.4] (n=43), closed_5p 17.9% [9.3, 27.1] (n=603), later -46.6% [-72.3, 3.0] (n=10)

Alameda, Cleanup Program (n = 10,730): open 28.2% [5.3, 56.1] (n=160), closed_0_2 49.0% [3.3, 114.9] (n=17), closed_2_5 37.7% [-15.5, 124.4] (n=14), closed_5p 25.8% [7.6, 47.0] (n=99), later 55.7% [16.7, 107.6] (n=51)

Alameda, median $ per lot sq ft by treatment: closed_0_2 56, closed_2_5 92, closed_5p 64, control 52, later 61, open 52

### Pooled across counties (inverse-variance weights on the M1 coefficients)

| case class      | treatment   |    n |   pooled % | 95% CI       | by county                                                                     |
|:----------------|:------------|-----:|-----------:|:-------------|:------------------------------------------------------------------------------|
| Cleanup Program | open        |  712 |        7   | [0.5, 13.9]  | Los Angeles 4.8% (n=552); Alameda 28.3% (n=160)                               |
| Cleanup Program | closed_0_2  |   75 |       20   | [1.5, 41.9]  | Los Angeles 13.3% (n=58); Alameda 49.0% (n=17)                                |
| Cleanup Program | closed_2_5  |   64 |       25.2 | [4.7, 49.8]  | Los Angeles 23.4% (n=50); Alameda 37.7% (n=14)                                |
| Cleanup Program | closed_5p   | 1119 |        2.1 | [-2.4, 6.8]  | Los Angeles 0.2% (n=1020); Alameda 25.7% (n=99)                               |
| LUST            | open        | 1064 |        5.4 | [-0.2, 11.4] | Los Angeles 6.1% (n=929); San Francisco 7.4% (n=12); Alameda -0.1% (n=123)    |
| LUST            | closed_0_2  |  329 |       13.1 | [4.2, 22.8]  | Los Angeles 11.0% (n=274); San Francisco 14.1% (n=10); Alameda 26.0% (n=45)   |
| LUST            | closed_2_5  |  388 |       14.7 | [6.6, 23.4]  | Los Angeles 11.1% (n=335); San Francisco -4.8% (n=10); Alameda 50.1% (n=43)   |
| LUST            | closed_5p   | 3040 |       11.5 | [7.7, 15.5]  | Los Angeles 10.2% (n=2270); San Francisco 6.5% (n=167); Alameda 17.8% (n=603) |
| all             | open        | 1777 |        6.4 | [2.0, 11.0]  | Los Angeles 5.4% (n=1481); San Francisco 21.4% (n=13); Alameda 14.7% (n=283)  |
| all             | closed_0_2  |  404 |       14.4 | [6.3, 23.1]  | Los Angeles 11.3% (n=332); San Francisco 15.4% (n=10); Alameda 31.8% (n=62)   |
| all             | closed_2_5  |  453 |       15.3 | [7.8, 23.4]  | Los Angeles 12.0% (n=385); San Francisco -3.8% (n=10); Alameda 45.1% (n=58)   |
| all             | closed_5p   | 4161 |        9.4 | [6.3, 12.6]  | Los Angeles 7.4% (n=3290); San Francisco 6.7% (n=168); Alameda 19.0% (n=703)  |
