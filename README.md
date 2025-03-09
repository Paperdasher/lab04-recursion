# lab04-recursion

## Numbers into English words

toWords(14) returns "fourteen"

toWords(94) returns "ninety-four"

toWords(342) returns "three hundred and forty-two" (note the and)

toWords(115) returns "one hundred and fifteen"

toWords(100) returns "one hundred"

toWords(0) returns "zero" note this is the only time you ever say zero.

### The use of AND

The use of "and" when writing out numbers is in compliance with British usage. Always use "and" between the word "hundred" and the ones/tens part of that number. "one hundred and ten" or "six hundred and forty-two"

### Scaling Numbers

You need some base cases then build up the numbers from there.

999 is the starting point for larger numbers.

Once you get 0-999, you can easily extend the program to work for thousands/millions/billions/trillions/etc.)

999,999,999 or x,y,z is written as: x million y thousand z

1,012,401 is written as: one million twelve thousand four hundred and one

999,000,999 or x,y,z is written as: x million z

### Groups:

Each 3 digit grouping is included in your 0-999 code. You just need a suffix.

You can include: thousand, million, billion to allow any 32 bit int to be included.

You never say groups that are all zero, so : 1,000,442 is spoken as: "one million four hundred and forty-two"

Since zero is a special case, a wrapper method could be useful! (0 is zero, but 1,000,000 is NOT one million zero thousand and zero)


### Negative values:

You can allow negative numbers as well.

-2,123,000,999 or -w,x,y,z is written as: "negative w billion x million z" or specifically: "negative two billion one hundred and twenty-three million nine hundred and ninety-nine"
