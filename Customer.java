import java.util.Scanner;
import java.util.ArrayList;  //even if we use an Array List in a method to access another Array List in another class, we should import it in the cuurrent method.

// -> commented code
//__ -> Explanation and/or idea

public class Customer {//------------
	private String name;
	public String email;
	public String phone_number;
  private double card = 0;
	private String card_info; //for payment information

  //********* Address **********
  //public String country;
  public String address;
  public String city;
  public String state;
  public String zipcode;

  //Contructor
  public Customer (String name, Cart itemsInCart){
    this.name = name;
    System.out.println();
    System.out.println("Name: "+this.name);
    System.out.print("Items in the Cart: ");
    itemsInCart.the_itemsInCart();
    System.out.println();
  }

  //******** Functions ***********
	public void add_to_cart(Item item, Cart addToCart){
    addToCart.add_item(item); //call from Cart.java
	}
	public void removeAnItem(int index, Cart removeFromCart){
		removeFromCart.remove_item(index);
  }
  public void clear_cart(Cart cart){ //removes all items
    cart.clearCart();
  }
  //__trying to add to the variable "card" to buy items, otherwise I would make a "Card class"
  public void addMoneyToCart(double add_money){
    this.card += add_money;
  }
  public double getCardBalance(){
    return this.card;
  }
  /*to check_out:
    
    make a method about asking for card_info, then make another method for     check_out and ask with if-statement if the card_info was introduced before checking out.
    
    */
  public void typeCardinfo(){  //Typing card information
    Scanner forName = new Scanner(System.in);
    Scanner cardNumber = new Scanner(System.in);
    Scanner expire_date = new Scanner(System.in);
    Scanner forCVV = new Scanner(System.in);

    System.out.print("Name on Card: ");
    String _name = forName.nextLine();

    System.out.print("Card Number: ");
    this.card_info = cardNumber.nextLine();

    System.out.print("Expiration Date (MM/YY): ");
    String expireDate = expire_date.nextLine();

    System.out.print("CVV: ");
    int cvv = forCVV.nextInt();

    forName.close();
    cardNumber.close();
    expire_date.close();
    forCVV.close();
    
  }  //now make the check_out method!
  public void check_out(Cart forTotal){
    //an ArrayList for purchaseHistory
    double total = forTotal.getTotalPrice();
    this.typeCardinfo();
    if(this.card > 0){ //if-statement part 1
      if(this.card >= total){ //if-statement part 2
        this.card -= total;
        System.out.println("Your order is on your way!");
      } else{ //else-statement part 2
          System.out.println("You do not have enough balance to make this purchase");
        }
    } else{ //else-statement part 1
      System.out.println("There is no balance on your account");
    }
    //adding to purchaseHistory
  }
  public void display_items(Cart from_cart){
    ArrayList<Item> in_cart = from_cart.getListItems();

    System.out.println();
    for(Item item: in_cart){
      System.out.println(item.getName());
    }
    System.out.println();
  }
  //public void purchase_history(){}
 //**Try to create the purchase_history from within the check_out method**
   //__display items
  public void address(String address, String city, String state, String zipcode){
    this.address = address;
    this.city = city;
    this.state = state;
    this.zipcode = zipcode;
  }
  public String get_address(){
    return this.address+" ,"+this.city+" ,"+this.state+" ,"+this.zipcode;
  }
}//---------------