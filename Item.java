// -> commented code
//__ -> Explanation and/or idea

public class Item { //class creation
    public String category; //type of item
    private double price;
    public String name;
    private String product_id;
    private int quantity;
    public String description;
  
    //Constructor
    public Item (double price, String name, String category){
      //add a "switch-statement based on the type of items, then in every case, different prices."
      this.price = price;
      this.name = name;
      this.category = category;
    }
  
    //******** Functions ***********
    public void add_quantity(int quantity){
      this.quantity =+ quantity;
      this.price = this.price * quantity;
    }
      public void remove_quantity(int quantity) {  //Analyze this more for logical function
        if (quantity > this.quantity) {
              System.out.println("Cannot remove more than available quantity.");
        }
  
          this.quantity -= quantity;
          this.price /= quantity;
    }
    public void details(String description){
      this.description = description;
      System.out.println("Description: "+description+"$"+this.price);
    }
    public String getName(){
      return this.name;
    }
    public void update_quantity(){ //return number of items after being added to or removed from
      System.out.println(this.quantity+" units");
    }
    public void change_price(int price){
      this.price = price;
    }
    /* public void item_quantity(int quant){
      this.price *= quant;
    }*/
    public double get_price(){
      return price;
    }
  }  //end of class
  
  //__A Switch-statement that may work as to choosing item-type or color, and depending on that, modifying the price of it