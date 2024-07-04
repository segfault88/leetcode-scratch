#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

fn main() {
    let x = vec!(ListNode::new(123));

    println!("{:?}", x)
}

#[test]
fn foo() {
    let x = vec!(ListNode::new(123));

    assert_eq!(x, vec!(ListNode::new(123)));
}
