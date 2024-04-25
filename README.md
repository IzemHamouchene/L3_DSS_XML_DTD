# TP 1 : DTD manipulation

In this exercise, you will write XML files dependding of DTD rules.

## Exercise 1 : Write XML files
Edit all XML files stat start with _1_ to follow the DTDs illustrated in the following table:

| DTD rules | XML file
| --- | --- |
| a <br/> b | x1 |
| \* <!DOCTYPE INVENTAIRE [ <br/> <!ELEMENT INVENTAIRE (TITRE)> <br/> <!ELEMENT TITRE (#PCDATA | SOUSTITRE)*> <br/> <!ELEMENT SOUSTITRE (#PCDATA)> ]> | 1_input_1.xml |

| <!DOCTYPE INVENTAIRE [
<!ELEMENT INVENTAIRE (TITRE)*>
<!ELEMENT TITRE (#PCDATA | SOUSTITRE)>
<!ELEMENT SOUSTITRE (#PCDATA)> ]> | 1_input_2.xml |

| <!DOCTYPE INVENTAIRE [
<!ELEMENT INVENTAIRE (TITRE)>
<!ELEMENT TITRE (#PCDATA, SOUSTITRE)*>
<!ELEMENT SOUSTITRE (#PCDATA)> ]> | 1_input_3.xml |


     
  Check the Actions tab to see if you have completed the exercise successfully.
