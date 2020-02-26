module display_decoder(
    input  wire clk,
   output wire A,
 output wire B,
output wire C,
output wire D,
input wire a,
input wire b,
input wire c,
input wire d,    
);
always @(posedge clk) begin
  
  A=a;
  B=b;
  C=c;
  D=d;
  
 end
  
endmodule