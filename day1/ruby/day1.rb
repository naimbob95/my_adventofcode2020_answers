

def readinputfiles(file_path)
    array = []
    File.open(file_path).each_line do |line|
        array.push(Integer(line.chomp)) 
    end
    array 
end

def findthenum(all_num)
    array = []
    cond = true
    while cond 
        # statements to be executed 
        p1, p2 = all_num.sample(2)
        ans = p1 + p2
        if ans == 2020
            array.push(p1)
            array.push(p2)
            cond = false
        else
            next
        end
    end
    array
end


def findthenum2(all_num)
    array = []
    cond = true
    while cond 
        # statements to be executed 
        p1, p2,p3 = all_num.sample(3)
        ans = p1 + p2 + p3
        if ans == 2020
            array.push(p1)
            array.push(p2)
            array.push(p3)
            cond = false
        else
            next
        end
    end
    array
end

##part1
file_path = "input.txt"
all_num = readinputfiles(file_path)
result = findthenum(all_num)
ans_part1 = result[0]*result[1]
puts "The answer for part1: #{ans_part1}"

##part2
result2 = findthenum2(all_num)
ans_part2 = result2[0]*result2[1]*result2[2]
puts "The answer for part2: #{ans_part2}"