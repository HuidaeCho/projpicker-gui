#!/bin/sh
set -e

cleanup() {
	rm -f *.tmp
}
trap cleanup EXIT

echo -n "test_pyproj.py..." | tee run.tmp
python3 test_pyproj.py > test.tmp
if diff test.tmp test_pyproj.out > /dev/null; then
	echo "PASSED" | tee -a run.tmp
else
	echo "FAILED" | tee -a run.tmp
fi

for infile in *.txt; do
	outfile=$(echo $infile | sed 's/txt$/out/')

	echo -n "-i $infile..." | tee -a run.tmp
	opts=$(sed '/^#opts: /!d; s/^#opts: //' $infile)
	../projpicker.py $opts -i $infile > test.tmp
	if diff test.tmp $outfile > /dev/null; then
		echo "PASSED" | tee -a run.tmp
	else
		echo "FAILED" | tee -a run.tmp
	fi

	args=$(sed '/^#args: /!d; s/^#args: //' $infile)
	if [ "$args" != "" ]; then
		echo -n "$args..." | tee -a run.tmp
		eval "../projpicker.py $args" > test.tmp
		if diff test.tmp $outfile > /dev/null; then
			echo "PASSED" | tee -a run.tmp
		else
			echo "FAILED" | tee -a run.tmp
		fi
	fi

	python=$(sed '/^#python$/,/^#end$/!d; /^#\(python\|end\)$/d; s/^# //' $infile)
	if [ "$python" != "" ]; then
		echo -n "python $infile..." | tee -a run.tmp
		echo "$python" | python3 > test.tmp
		if diff test.tmp $outfile > /dev/null; then
			echo "PASSED" | tee -a run.tmp
		else
			echo "FAILED" | tee -a run.tmp
		fi
	fi
done

passed=$(grep "PASSED$" run.tmp | wc -l)
failed=$(grep "FAILED$" run.tmp | wc -l)

cat<<EOT

PASSED: $passed
FAILED: $failed
EOT