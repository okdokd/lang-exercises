use std::io;

fn main() {
    let mut i = String::new();
    io::stdin().read_line(&mut i).unwrap();
    let i: i32 = i.trim().parse().unwrap();

    println!("{}", i.pow(3));
}