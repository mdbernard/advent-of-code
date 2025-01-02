use std::cmp::{max, min};

fn parse_input() -> (Vec<u32>, Vec<u32>) {
    let input_file = std::fs::read_to_string("input.txt").expect("File can't be read");

    let mut list_1: Vec<u32> = vec![];
    let mut list_2: Vec<u32> = vec![];

    for line in input_file.lines() {
        let split: Vec<&str> = line.split_whitespace().collect();
        if split.len() != 2 {
            panic!("All lines must contain two numbers separated by whitespace");
        }
        list_1.push(split[0].parse().expect("Malformed line"));
        list_2.push(split[1].parse().expect("Malformed line"));
    }

    return (list_1, list_2);
}

fn part_1(mut list_1: Vec<u32>, mut list_2: Vec<u32>) -> u32 {
    list_1.sort();
    list_2.sort();

    // PART 1
    let total_distance: u32 = list_1
        .iter()
        .zip(list_2.iter())
        .map(|(first, second)| max(first, second) - min(first, second))
        .sum();


    return total_distance;
}

fn part_2(list_1: Vec<u32>, list_2: Vec<u32>) -> u32 {
    let mut similarity: u32 = 0;

    for number in list_1.iter() {
        similarity += number * list_2.iter().filter(|&value| value == number).count() as u32;
    }

    return similarity;
}

fn main() {
    // INPUT PROCESSING
    let (list_1, list_2) = parse_input();
    println!("Part 1: {}", part_1(list_1.clone(), list_2.clone()));
    println!("Part 2: {}", part_2(list_1.clone(), list_2.clone()));
}

#[cfg(test)]
mod tests {
    use super::{part_1, part_2};

    #[test]
    fn test_part_1() {
        // given example
        let list_1: Vec<u32> = vec![3, 4, 2, 1, 3, 3];
        let list_2: Vec<u32> = vec![4, 3, 5, 3, 9, 3];
        assert_eq!(part_1(list_1, list_2), 11);
    }

    #[test]
    fn test_part_2() {
        // given example
        let list_1: Vec<u32> = vec![3, 4, 2, 1, 3, 3];
        let list_2: Vec<u32> = vec![4, 3, 5, 3, 9, 3];
        assert_eq!(part_2(list_1, list_2), 31);
    }
}
