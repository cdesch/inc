
# Examples

    echo "foo foo quux labs foo bar quux" | /home/hduser/mapper.py
    echo "foo foo quux labs foo bar quux" | /home/hduser/mapper.py | sort -k1,1 | /home/hduser/reducer.py
    cat /tmp/gutenberg/20417-8.txt | /home/hduser/mapper.py
# Run

    echo "foo foo quux labs foo bar quux" | python mapper.py
    echo "foo foo quux labs foo bar quux" | python mapper.py | sort -k1,1 | /home/hduser/reducer.py
    cat sampledata.csv | python mapper.py 
    cat sampledata.csv | python mapper.py | sort -k1,1 | python reducer.py

 =concatenate(RANDBETWEEN(DATE(2019,1,1),DATE(2019,3,24))," ",TIME(7,RANDBETWEEN(0,104),RANDBETWEEN(0,59)))