# ML Algorithms Oxidized

## Find-S

```rust
pub fn find_s(training: &Vec<I>) -> H {
    let mut h: H = H::new();
    for x: &I in training.into_iter() {
        for a: &A in x.attrs.into_iter() {
            if !h.satisfy(a) {
                h = h.more_generic_on(a)
            }
        }
    }
    h
}
```

## ID3

```rust
pub fn id3(tree: &mut T, training: &Vec<I>, attrs: &[A]) -> T {
    if attrs.size > 0 {
        let attr: A = elect_by_max_ig(training, attrs);
        tree.set_root(N::from_attr(attr));
        for v: V in attr.values.into_iter() {
            let D: Vec<I> = training.filter(|x| {x.get<attr>() == v});
            let n_attrs = attrs.filter(|x| {x != attr});
            tree.add_sub_tree(id3(&N::new().as_tree(), &D, &n_attrs));
        }
    } else {
        node = N::from_label(elect_label(training));
        tree.set_root(node);
    }
    tree
}
```
