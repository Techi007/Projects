import java.util.ArrayList;

// -> commented code
//__ -> Explanation and/or idea

public class Cart {
  //__the items on the cart = items
	private ArrayList<Item> items = new ArrayList<>();
	private double total_price;
	//public int item_count;

  //Constructor
  public Cart(){//current number of items in Cart
    this.items.size();
  }
  //******** Functions **********
	public void add_item(Item item){
		items.add(item);
	}
  // *declare a method to return the quantity of items in the Cart
	public void remove_item(int index){
    this.items.remove(index);
		//__maybe to add an if statement for the user to not get out of bound, and/or also to use the object in the parameter instead of an index number.
  }
  public void clearCart(){
    this.items.clear();
  }
  
  public void the_itemsInCart(){//return quantity of items
    System.out.println(this.items.size()+ " items");
  }
  public double calc_total(){ //calculating total price
    this.total_price = 0;
    for(Item item: this.items){
      total_price += item.get_price();
    }
    return total_price;
  }
  public double getTotalPrice(){
    return this.total_price;
  }
  
	public ArrayList<Item> getListItems(){
    return items;
  }
}